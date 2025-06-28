import os
import random
import pandas as pd

# Define the directory path
directory_path = "path/to/directory"  # Replace with the actual path to your directory

# Output Excel file name
output_xlsx = "java-deepseek-33B-instruct-awq.xlsx"

# Get all files in the directory
all_files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Randomly select up to 50 files
selected_files = random.sample(all_files, min(50, len(all_files)))

# Prepare data for Excel
data = []
for idx, file_name in enumerate(selected_files):
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, "r", encoding="utf-8") as file:
        code_content = file.read()

    # Append data with empty consistency and readability columns
    data.append([f"task_{idx+1}", code_content, "", ""])  # Blank values for consistency & readability

# Create a DataFrame
df = pd.DataFrame(data, columns=["taskid", "code", "consistency", "readability"])

# Save to Excel
df.to_excel(output_xlsx, index=False)

print(f"Excel file '{output_xlsx}' created successfully with {len(data)} entries.")
