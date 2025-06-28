import os
import pandas as pd

# Define the input Excel file path
input_file = "path/to/.xlsx"

# Define the output directory and CSV file path
output_directory = "path/to/directory"  # Replace with the actual path to your directory
output_csv_path = os.path.join(output_directory, "r-flake8_33b-fp.csv")

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the Excel file
df = pd.read_excel(input_file)

# Extract relevant columns
df_filtered = df[["Task ID", "ERROR", "WARNING", "PyFlakes"]].copy()

# Function to count the number of error codes in each column
def count_errors(column):
    return column.fillna("").apply(lambda x: len(x.split("\n")) if x.strip() else 0)

# Apply the counting function to each category
df_filtered["ERROR"] = count_errors(df_filtered["ERROR"])
df_filtered["WARNING"] = count_errors(df_filtered["WARNING"])
df_filtered["PyFlakes"] = count_errors(df_filtered["PyFlakes"])

# Extract the numeric part of the task ID (e.g., taskid-123 from taskid-123_some_text)
#df_filtered["Task ID Numeric"] = df_filtered["Task ID"].str.extract(r'taskid-(\d+)').astype(int)
df_filtered["Task ID Numeric"] = df_filtered["Task ID"].str.extract(r'Python-(\d+)').astype(int)

# Sort by extracted numeric task ID
df_filtered = df_filtered.sort_values(by=["Task ID Numeric"])

# Drop the temporary sorting column
df_filtered = df_filtered.drop(columns=["Task ID Numeric"])

# Save to CSV
df_filtered.to_csv(output_csv_path, index=False)

print(f"CSV file successfully saved at: {output_csv_path}")
