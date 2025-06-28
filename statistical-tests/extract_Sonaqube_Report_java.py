import requests
import pandas as pd
import json
import os
import re

# SonarCloud API Configuration
SONAR_TOKEN = '0000000000000000000000'  # Replace with your SonarCloud token
PROJECT_KEY = 'username_SonarQube-Analysis-java'       # Replace with your SonarCloud project key
SONAR_URL = 'https://sonarcloud.io'

# Directory to filter (relative to project root)
#TARGET_DIRECTORY = 'mc-java-codellama7B-AWQ-all'  # Example: 'py-codellama7B-AWQ-all'
#TARGET_DIRECTORY = 'mc-java-codellama7B-AWQ-all'
TARGET_DIRECTORY = 'java-deepseek1.3B-AWQ-all'

# Issue Types to Count
ISSUE_TYPES = ['BUG', 'VULNERABILITY', 'CODE_SMELL']

# Metrics to extract
METRICS = [
    'ncloc',                      # Lines of Code
    'complexity',                 # Cyclomatic Complexity
    'cognitive_complexity'        # Cognitive Complexity
]

# Function to fetch issues per file
def fetch_issues_for_file(file_key):
    url = f"{SONAR_URL}/api/issues/search"
    params = {
        'componentKeys': file_key,
        'ps': 500,  # Max page size
        'facets': 'types',  # Get counts per issue type
    }
    response = requests.get(url, auth=(SONAR_TOKEN, ''), params=params)

    if response.status_code != 200:
        print(f"Error fetching issues for {file_key}: {response.status_code} - {response.text}")
        return {issue_type: 0 for issue_type in ISSUE_TYPES}

    data = response.json()
    issue_counts = {issue_type: 0 for issue_type in ISSUE_TYPES}

    # Extracting issues from 'facets'
    facets = data.get('facets', [])
    for facet in facets:
        if facet['property'] == 'types':
            for value in facet['values']:
                issue_type = value['val']
                if issue_type in issue_counts:
                    issue_counts[issue_type] = value['count']

    # Explicitly fetch Security Hotspots (since facets may not return it correctly)
    security_hotspots_url = f"{SONAR_URL}/api/hotspots/search"
    security_params = {
        'projectKey': PROJECT_KEY,
        'componentKeys': file_key,
        'ps': 500,  # Max page size
    }
    sec_response = requests.get(security_hotspots_url, auth=(SONAR_TOKEN, ''), params=security_params)

    if sec_response.status_code == 200:
        sec_data = sec_response.json()
        issue_counts['SECURITY_HOTSPOT'] = sec_data.get('total', 0)  # Get total security hotspots count

    return issue_counts


# Function to fetch all files with metrics, handling pagination
def fetch_all_files_with_metrics():
    all_components = []
    page = 1
    page_size = 500  # SonarCloud API limit

    while True:
        url = f"{SONAR_URL}/api/measures/component_tree"
        params = {
            'component': PROJECT_KEY,
            'metricKeys': ','.join(METRICS),
            'ps': page_size,
            'p': page,
            'qualifiers': 'FIL'  # Only files
        }
        response = requests.get(url, auth=(SONAR_TOKEN, ''), params=params)

        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code} - {response.text}")
            return []

        data = response.json()
        components = data.get('components', [])
        all_components.extend(components)

        if len(components) < page_size:
            break  # No more pages
        else:
            page += 1

    return all_components

# Extract taskid from file path
def extract_taskid(file_path):
    # Match taskid directories like taskid-9
    match = re.search(r'(taskid-\d+)', file_path)
    if match:
        taskid = match.group(1)
        return os.path.join(os.path.dirname(file_path.split(match.group(0))[0]), taskid)
    return None

# Sort taskids numerically
def sort_taskids(taskid_list):
    def extract_number(taskid):
        match = re.search(r'taskid-(\d+)', taskid)
        return int(match.group(1)) if match else float('inf')
    return sorted(taskid_list, key=extract_number)

'''# Extract taskid from file path (modified for "Java-1-gen0.java" format)-> mceval
def extract_taskid(file_path):
    filename = os.path.basename(file_path)  # Extract file name
    match = re.match(r'Java-(\d+)-gen\d+\.java', filename)  # Match pattern "Java-1-gen0.java"
    if match:
        taskid = f"Java-{match.group(1)}"
        return taskid
    return None


# Sort taskids numerically
def sort_taskids(taskid_list):
    def extract_number(taskid):
        match = re.search(r'Java-(\d+)', taskid)
        return int(match.group(1)) if match else float('inf')
    return sorted(taskid_list, key=extract_number)'''



# Process the data and aggregate by taskid
def process_data_by_taskid(components, target_directory):
    taskid_aggregates = {}
    totals = {
        'LoC': 0,
        #'Security': 0,
        'Reliability': 0,
        'Maintainability': 0,
        'Security_Hotspots': 0,
        #'Bugs': 0,
        #'Code Smells': 0,
        'CyC': 0,
        'CoC': 0
    }

    for comp in components:
        file_path = comp.get('path', 'Unknown')
        file_key = comp.get('key', '')

        if not file_path.startswith(target_directory):
            continue  # Skip files not in the target directory

        # Extract taskid
        taskid_dir = extract_taskid(file_path)
        if not taskid_dir:
            continue  # Skip if no valid taskid found

        # Initialize taskid aggregate if not exists
        if taskid_dir not in taskid_aggregates:
            taskid_aggregates[taskid_dir] = {
                'TaskID': taskid_dir,
                'LoC': 0,
                #'Security': 0,
                'Reliability': 0,
                'Maintainability': 0,
                'Security_Hotspots': 0,
                #'Bugs': 0,
                #'Code Smells': 0,
                'CyC': 0,
                'CoC': 0
            }

        # Initialize all metrics
        measures = {metric: 0 for metric in METRICS}

        # Update measures with actual values from API
        for m in comp.get('measures', []):
            measures[m['metric']] = float(m.get('value', 0))

        # Fetch issue counts for the file
        issue_counts = fetch_issues_for_file(file_key)

        # Aggregate metrics for taskid
        taskid_data = taskid_aggregates[taskid_dir]
        taskid_data['LoC'] += measures.get('ncloc', 0)
        taskid_data['CyC'] += measures.get('complexity', 0)
        taskid_data['CoC'] += measures.get('cognitive_complexity', 0)
        #taskid_data['Security'] += issue_counts.get('VULNERABILITY', 0)
        taskid_data['Reliability'] += issue_counts.get('BUG', 0)
        taskid_data['Maintainability'] += issue_counts.get('CODE_SMELL', 0)
        taskid_data['Security_Hotspots'] += issue_counts.get('SECURITY_HOTSPOT', 0)
        #taskid_data['Bugs'] += issue_counts.get('BUG', 0)
        #taskid_data['Code Smells'] += issue_counts.get('CODE_SMELL', 0)

    # Calculate totals from taskid aggregates
    for taskid_data in taskid_aggregates.values():
        for key in totals.keys():
            totals[key] += taskid_data.get(key, 0)

    # Sort taskids numerically
    sorted_taskids = sort_taskids(list(taskid_aggregates.keys()))
    sorted_aggregates = [taskid_aggregates[tid] for tid in sorted_taskids]

    return sorted_aggregates, totals

# Main execution
if __name__ == "__main__":
    print("Fetching files from SonarCloud (this may take a while for large projects)...")
    components = fetch_all_files_with_metrics()
    if not components:
        print("No data fetched.")
        exit(1)

    print(f"Total files fetched: {len(components)}")

    taskid_data_rows, totals = process_data_by_taskid(components, TARGET_DIRECTORY)
    
    if not taskid_data_rows:
        print(f"No files found in directory: {TARGET_DIRECTORY}")
        exit(1)

    print(f"Total taskids processed in '{TARGET_DIRECTORY}': {len(taskid_data_rows)}")

    df = pd.DataFrame(taskid_data_rows)

    # Export to CSV
    csv_file = f'{TARGET_DIRECTORY.replace("/", "_")}.csv'
    df.to_csv(csv_file, index=False)
    print(f"CSV report saved as {csv_file}")

    # Export to JSON in horizontal format
    json_file = f'{TARGET_DIRECTORY.replace("/", "_")}.json'
    with open(json_file, 'w') as jf:
        for row in taskid_data_rows:
            json.dump(row, jf)
            jf.write('\n')  # Write each JSON object in a single line

        # Write totals as the last line
        totals_row = {'TOTALS': {k: str(v) for k, v in totals.items()}}
        json.dump(totals_row, jf)
        jf.write('\n')

    print(f"JSON report saved as {json_file}")
