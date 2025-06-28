import os
import json

def process_json_files(input_folder):
    # Create the output folder named "python-files" inside the input folder
    output_folder = os.path.join(input_folder, "python-files")
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all JSON files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            filepath = os.path.join(input_folder, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)

            # Extract the task ID from the filename (e.g., HumanEval_0 -> taskid-0)
            task_id = filename.split('.')[0].replace('HumanEval_', 'taskid-')

            # Process each program in the JSON file
            for i, result in enumerate(data.get('results', [])):
                program_code = result.get('program', '')

                # Extract code until "def check(candidate):" is found
                program_code_extracted = program_code.split("def check(candidate):")[0]

                # Construct the Python file name
                python_filename = f"{task_id}-gen{i}.py"
                output_path = os.path.join(output_folder, python_filename)

                # Write the extracted program code to the output folder
                with open(output_path, 'w') as python_file:
                    python_file.write(program_code_extracted)

    print(f"Python files saved in: {output_folder}")


if __name__ == "__main__":
    # Specify the input folder
    input_folder = "path to the folder containing JSON files"

    # Process the JSON files
    process_json_files(input_folder)
