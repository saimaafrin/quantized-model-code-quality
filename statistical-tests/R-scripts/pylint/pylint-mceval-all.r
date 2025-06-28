rm(list=ls())

# Download the required libraries if not installed
if (!require("effsize")) install.packages("effsize")
library(effsize)

# Manually specify file paths
FP_paths <- list(
  "CodeLlama-7B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_7b-fp.csv",
  "CodeLlama-13B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_13b-fp.csv",
  "CodeLlama-34B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_34b-fp.csv",
  "DeepSeek-Coder-1.3B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_1.3b-fp.csv",
  "DeepSeek-Coder-6.7B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_6.7b-fp.csv",
  "DeepSeek-Coder-33B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_33b-fp.csv"
)

AWQ_paths <- list(
  "CodeLlama-7B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_7b-awq.csv",
  "CodeLlama-13B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_13b-awq.csv",
  "CodeLlama-34B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_34b-awq.csv",
  "DeepSeek-Coder-1.3B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_1.3b-awq.csv",
  "DeepSeek-Coder-6.7B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_6.7b-awq.csv",
  "DeepSeek-Coder-33B" = "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/r-pylint_33b-awq.csv"
)


# Metrics to compare
metrics <- c("Error", "Warning", "Convention", "Refactor")

# Function to check if a column is constant
is_constant <- function(x) {
  return(length(unique(x)) == 1)
}

# Wilcoxon test function
wilcox_test <- function(x, y) {
  if (is_constant(x) & is_constant(y)) {
    return(NA)
  }
  return(wilcox.test(x, y, alternative="two.side", paired=TRUE, exact=FALSE, correct=FALSE)$p.value)
}

# Iterate through model pairs
for (model in names(FP_paths)) {
  print(paste("**********************", model, "FP vs AWQ Comparison *********************************"))
  
  # Load datasets
  FP_data <- read.csv(FP_paths[[model]], header=TRUE)
  AWQ_data <- read.csv(AWQ_paths[[model]], header=TRUE)
  
  # Ensure both datasets have the same length
  min_length <- min(nrow(FP_data), nrow(AWQ_data))
  FP_data <- FP_data[1:min_length, ]
  AWQ_data <- AWQ_data[1:min_length, ]
  
  # Initialize results list
  res = list(Wilcoxon.p = c())
  
  # Perform Wilcoxon tests and Cliff's Delta
  for (metric in metrics) {
    print(paste("**********************", metric, "- FP vs AWQ (", model, ") *********************************"))
    #print("FP Data Summary:")
    #print(summary(FP_data[[metric]]))
    #print("AWQ Data Summary:")
    #print(summary(AWQ_data[[metric]]))
    res$Wilcoxon.p = append(res$Wilcoxon.p, wilcox_test(FP_data[[metric]], AWQ_data[[metric]]))
    print("Cliff's Delta:")
    print(cliff.delta(FP_data[[metric]], AWQ_data[[metric]]))
  }
  
  print("***************************************************************************")
  
  # Create data frame
  res_df = data.frame(Wilcoxon.p = res$Wilcoxon.p)
  res_df$Wilcoxon.p = p.adjust(res_df$Wilcoxon.p, method="holm")
  print(paste(model, "Results:"))
  print(res_df)
}
