import pandas as pd
from sklearn.metrics import cohen_kappa_score

def calculate_weighted_kappa(file_path_e1, file_path_e2):
    # Load CSV files
    df_e1 = pd.read_csv(file_path_e1)
    df_e2 = pd.read_csv(file_path_e2)

    # Merge both evaluator files on 'taskid'
    df_merged = df_e1.merge(df_e2, on="taskid", suffixes=("_E1", "_E2"))

    # Mapping categorical ratings to numerical values
    rating_map = {"good": 2, "acceptable": 1, "poor": 0}

    # Apply mapping to both evaluators' ratings
    df_merged["consistency_E1"] = df_merged["consistency_E1"].str.lower().map(rating_map)
    df_merged["consistency_E2"] = df_merged["consistency_E2"].str.lower().map(rating_map)
    df_merged["readability_E1"] = df_merged["readability_E1"].str.lower().map(rating_map)
    df_merged["readability_E2"] = df_merged["readability_E2"].str.lower().map(rating_map)

    # Compute Weighted Cohen’s Kappa for each attribute
    kappa_results = {}

    for attribute in ["consistency", "readability"]:
        kappa_linear = cohen_kappa_score(df_merged[f"{attribute}_E1"], df_merged[f"{attribute}_E2"], weights="linear")
        kappa_quadratic = cohen_kappa_score(df_merged[f"{attribute}_E1"], df_merged[f"{attribute}_E2"], weights="quadratic")
        kappa_results[attribute] = {
            "Linear Weighted Kappa": kappa_linear,
            "Quadratic Weighted Kappa": kappa_quadratic
        }

    return kappa_results

# Example usage:
file_path_e1 = "path/to/csv_file.csv"  
file_path_e2 = "path/to/csv_file.csv" 

results = calculate_weighted_kappa(file_path_e1, file_path_e2)

# Print results
print("Model: py-cl-34-awq\n")
for attr, scores in results.items():
    print(f"{attr.capitalize()} Kappa Scores:")
    #print(f"  Linear Weighted Kappa: {scores['Linear Weighted Kappa']:.4f}")
    print(f"  Quadratic Weighted Kappa: {scores['Quadratic Weighted Kappa']:.4f}\n")
