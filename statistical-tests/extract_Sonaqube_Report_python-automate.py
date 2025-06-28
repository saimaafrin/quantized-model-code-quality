import requests
import pandas as pd
import json
import os
import re

# SonarCloud API Configuration
SONAR_TOKEN = '000000000000000'  
PROJECT_KEY = 'username_sonarQube-analysis'  
SONAR_URL = 'https://sonarcloud.io'

# Issue Types to Count
ISSUE_TYPES = ['BUG', 'VULNERABILITY', 'CODE_SMELL']

# Metrics to extract
METRICS = [
    'ncloc',
    'complexity',
    'cognitive_complexity'
]

# Model directory prefixes
MODELS = [
    'codellama7B-AWQ', 'codellama13B-AWQ', 'codellama34B-AWQ',
    'deepseekcoder-1.3B-AWQ', 'deepseekcoder-6.7B-AWQ', 'deepseekcoder-33B-AWQ'
]

# Function to fetch issues per file
def fetch_issues_for_file(file_key):
    url = f"{SONAR_URL}/api/issues/search"
    params = {
        'componentKeys': file_key,
        'ps': 500,
        'facets': 'types'
    }
    response = requests.get(url, auth=(SONAR_TOKEN, ''), params=params)

    if response.status_code != 200:
        print(f"Error fetching issues for {file_key}: {response.status_code} - {response.text}")
        return {issue_type: 0 for issue_type in ISSUE_TYPES}

    data = response.json()
    issue_counts = {issue_type: 0 for issue_type in ISSUE_TYPES}
    facets = data.get('facets', [])
    for facet in facets:
        if facet['property'] == 'types':
            for value in facet['values']:
                issue_type = value['val']
                if issue_type in issue_counts:
                    issue_counts[issue_type] = value['count']

    # Fetch Security Hotspots
    sec_url = f"{SONAR_URL}/api/hotspots/search"
    sec_params = {'projectKey': PROJECT_KEY, 'componentKeys': file_key, 'ps': 500}
    sec_response = requests.get(sec_url, auth=(SONAR_TOKEN, ''), params=sec_params)
    if sec_response.status_code == 200:
        sec_data = sec_response.json()
        issue_counts['SECURITY_HOTSPOT'] = sec_data.get('total', 0)

    return issue_counts

# Function to fetch all file components with metrics
def fetch_all_files_with_metrics():
    all_components = []
    page = 1
    while True:
        url = f"{SONAR_URL}/api/measures/component_tree"
        params = {
            'component': PROJECT_KEY,
            'metricKeys': ','.join(METRICS),
            'ps': 500,
            'p': page,
            'qualifiers': 'FIL'
        }
        response = requests.get(url, auth=(SONAR_TOKEN, ''), params=params)
        if response.status_code != 200:
            print(f"Error fetching data: {response.status_code} - {response.text}")
            return []
        data = response.json()
        comps = data.get('components', [])
        all_components.extend(comps)
        if len(comps) < 500:
            break
        page += 1
    return all_components

def extract_taskid(file_path):
    match = re.search(r'Python-(\d+)-gen\d+\.py', os.path.basename(file_path))
    return f"Python-{match.group(1)}" if match else None

def sort_taskids(taskid_list):
    def extract_number(taskid):
        match = re.search(r'Python-(\d+)', taskid)
        return int(match.group(1)) if match else float('inf')
    return sorted(taskid_list, key=extract_number)

# Aggregation function
def process_data_by_taskid(components, target_directory):
    taskid_aggregates = {}
    totals = {'LoC': 0, 'Reliability': 0, 'Maintainability': 0, 'Security_Hotspots': 0, 'CyC': 0, 'CoC': 0}

    for comp in components:
        file_path = comp.get('path', '')
        file_key = comp.get('key', '')
        if not file_path.startswith(target_directory):
            continue

        taskid = extract_taskid(file_path)
        if not taskid:
            continue

        if taskid not in taskid_aggregates:
            taskid_aggregates[taskid] = {'TaskID': taskid, 'LoC': 0, 'Reliability': 0, 'Maintainability': 0, 'Security_Hotspots': 0, 'CyC': 0, 'CoC': 0}

        measures = {m['metric']: float(m.get('value', 0)) for m in comp.get('measures', [])}
        issues = fetch_issues_for_file(file_key)

        taskid_aggregates[taskid]['LoC'] += measures.get('ncloc', 0)
        taskid_aggregates[taskid]['CyC'] += measures.get('complexity', 0)
        taskid_aggregates[taskid]['CoC'] += measures.get('cognitive_complexity', 0)
        taskid_aggregates[taskid]['Reliability'] += issues.get('BUG', 0)
        taskid_aggregates[taskid]['Maintainability'] += issues.get('CODE_SMELL', 0)
        taskid_aggregates[taskid]['Security_Hotspots'] += issues.get('SECURITY_HOTSPOT', 0)

    for t in taskid_aggregates.values():
        for k in totals: totals[k] += t[k]

    sorted_ids = sort_taskids(list(taskid_aggregates.keys()))
    return [taskid_aggregates[tid] for tid in sorted_ids], totals

# Main execution block
if __name__ == "__main__":
    print("Fetching SonarCloud files...")
    components = fetch_all_files_with_metrics()
    if not components:
        print("No data fetched.")
        exit(1)

    for model in MODELS:
        for i in range(1, 10):
            folder = f"mc-py-{model}-{i}"
            print(f"Processing folder: {folder}")
            taskid_rows, totals = process_data_by_taskid(components, folder)
            if not taskid_rows:
                print(f"No files found in {folder}")
                continue
            df = pd.DataFrame(taskid_rows)
            csv_path = f"{folder}.csv"
            df.to_csv(csv_path, index=False)
            print(f"Saved CSV: {csv_path}")
            json_path = f"{folder}.json"
            with open(json_path, 'w') as jf:
                for row in taskid_rows:
                    json.dump(row, jf)
                    jf.write('\n')
                json.dump({'TOTALS': {k: str(v) for k, v in totals.items()}}, jf)
                jf.write('\n')
            print(f"Saved JSON: {json_path}")
