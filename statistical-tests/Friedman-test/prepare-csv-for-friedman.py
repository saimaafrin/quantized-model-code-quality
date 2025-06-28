import os
import pandas as pd

# === TOOL SETTINGS ===
'''tools = {
    "pylint": {
        "metrics": ["Error", "Warning", "Convention", "Refactor"],
        "root": "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8",
        "prefix": "r-pylint"
    },
    "flake8": {
        "metrics": ["ERROR", "WARNING", "PyFlakes"],
        "root": "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8",
        "prefix": "r-flake8"
    },
    "sonarqube": {
        "metrics": ["Reliability", "Maintainability", "Security_Hotspots", "CyC", "CoC"],
        "root": "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/csv-sonarqube-mceval",
        "prefix": "mc-py"
    }
}'''

tools = {
    "pmd": {
        "metrics": ["Best_Practices", "Code_Style", "Design", "Error_Prone", "Multithreading", "Performance"],
        "root": "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8",
        "prefix": "r-pmd"
    },
    "sonarqube": {
        "metrics": ["Reliability", "Maintainability", "Security_Hotspots", "CyC", "CoC"],
        "root": "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/csv-sonarqube-mceval",
        "prefix": "mc-java"
    }
}

# === MODEL FOLDERS ===
'''models = {
    "CodeLlama-7B": "cl-7B-awq",
    "CodeLlama-13B": "cl-13B-awq",
    "CodeLlama-34B": "cl-34B-awq",
    "DeepSeek-Coder-1.3B": "dsc-1.3B-awq",
    "DeepSeek-Coder-6.7B": "dsc-6.7B-awq",
    "DeepSeek-Coder-33B": "dsc-33B-awq"
}'''

models = {
    "DeepSeek-Coder-1.3B": "dsc-1.3B-awq",
    "CodeLlama-7B": "cl-7B-awq"
    
}

# === PROCESS EACH TOOL ===
for tool_name, config in tools.items():
    print(f"\n==== Processing {tool_name.upper()} ====")
    metrics = config["metrics"]
    root_base = config["root"]
    prefix = config["prefix"]

    output_dir = os.path.join(root_base, f"prepared_friedman_{tool_name}")
    os.makedirs(output_dir, exist_ok=True)

    for model, subdir in models.items():
        model_path = os.path.join(root_base, subdir)
        generations = {}

        for i in range(1, 10):
            if tool_name in ["pylint", "flake8", "pmd"]:
                files = [f for f in os.listdir(model_path) if f.startswith(prefix) and f.endswith(f"awq-{i}.csv")]
            else:  # SonarQube
                model_tag = subdir.replace("cl-", "codellama").replace("dsc-", "deepseek").replace("B-awq", "B")
                #pattern = f"mc-py-{model_tag}-AWQ-{i}.csv"
                pattern = f"mc-java-{model_tag}-AWQ-{i}.csv"
                files = [f for f in os.listdir(model_path) if f == pattern]


            if not files:
                continue

            try:
                df = pd.read_csv(os.path.join(model_path, files[0]))
                generations[f"gen{i}"] = df
            except Exception as e:
                print(f"Skipping {files[0]}: {e}")

        for metric in metrics:
            valid_gens = {k: df[metric] for k, df in generations.items() if metric in df.columns}
            if len(valid_gens) < 2:
                continue

            min_len = min(len(v) for v in valid_gens.values())
            aligned_df = pd.DataFrame({k: v[:min_len].reset_index(drop=True) for k, v in valid_gens.items()})
            aligned_df.insert(0, "TaskID", [f"task-{j+1}" for j in range(min_len)])

            output_file = os.path.join(output_dir, f"{model.replace(' ', '_')}_{metric}.csv")
            aligned_df.to_csv(output_file, index=False)
            print(f"Saved: {output_file}")
