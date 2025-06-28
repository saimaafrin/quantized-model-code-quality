import os
import pandas as pd
from collections import defaultdict

# Define the input folder path
input_folder = "/home/user/projects/NonFunc-AWQ/mcEval-java/deepseekcoder-1.3B-instruct-awq-9/pmd"  # Replace with the actual folder path
#model_name = os.path.basename(os.path.dirname(os.path.dirname(input_folder)))
model_name = os.path.basename(os.path.dirname(input_folder))

# Define the output CSV file path
output_directory = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/dsc-1.3B-awq"
#output_csv_path = os.path.join(output_directory, "r-pmd_33b-fp.csv")
output_csv_path = os.path.join(output_directory, f"r-pmd_{model_name}.csv")

# Categories to track (mapping file suffix to proper column name)
category_mapping = {
    "bestpractices": "Best_Practices",
    "codestyle": "Code_Style",
    "design": "Design",
    "errorprone": "Error_Prone",
    "multithreading": "Multithreading",
    "performance": "Performance"
}

# Dictionary to store line counts per taskid
task_data = defaultdict(lambda: {category: 0 for category in category_mapping.values()})

# Process files in the folder
for filename in os.listdir(input_folder):
    #if filename.startswith("taskid-") and filename.endswith(".txt"):
    if filename.startswith("Java-") and filename.endswith(".txt"):
        parts = filename.rsplit("_", 1)  # Split into taskid and category
        taskid_full = parts[0]  # Extract full task ID (e.g., "taskid-81_numerical_letter_grade-gen0")
        category_key = parts[1].replace(".txt", "")  # Extract category key (e.g., "errorprone")

        if category_key in category_mapping:
            file_path = os.path.join(input_folder, filename)

            # Count the number of lines in the file
            with open(file_path, "r", encoding="utf-8") as f:
                line_count = sum(1 for _ in f)

            # Store the line count in the corresponding category
            task_data[taskid_full][category_mapping[category_key]] = line_count

# Convert dictionary to DataFrame
df = pd.DataFrame.from_dict(task_data, orient="index")
df.reset_index(inplace=True)
df.rename(columns={"index": "Task ID"}, inplace=True)

# Extract numeric part of task ID for sorting
#df["Task ID Numeric"] = df["Task ID"].str.extract(r'taskid-(\d+)').astype(int)
df["Task ID Numeric"] = df["Task ID"].str.extract(r'Java-(\d+)').astype(int)

# Sort by numeric task ID
df = df.sort_values(by=["Task ID Numeric"]).drop(columns=["Task ID Numeric"])

# Save to CSV
df.to_csv(output_csv_path, index=False)

print(f"CSV file successfully saved at: {output_csv_path}")
