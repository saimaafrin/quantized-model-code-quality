rm(list=ls())

# Download the required libraries if not installed
if (!require("effsize")) install.packages("effsize")
library(effsize)

# Load the Python datasets
FP_data_py <- read.csv("/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/py-deepseek1.3B-FP-all.csv", header=TRUE)
AWQ_data_py <- read.csv("/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/py-deepseek1.3B-AWQ-all.csv", header=TRUE)

# Load the Java datasets
FP_data_java <- read.csv("/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/sonarqube_taskid_aggregates_java-codellama7B-FP-all.csv", header=TRUE)
AWQ_data_java <- read.csv("/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/sonarqube_taskid_aggregates_java-codellama7B-AWQ-all.csv", header=TRUE)

# Ensure both datasets have the same length
min_length_py <- min(nrow(FP_data_py), nrow(AWQ_data_py))
FP_data_py <- FP_data_py[1:min_length_py, ]
AWQ_data_py <- AWQ_data_py[1:min_length_py, ]

min_length_java <- min(nrow(FP_data_java), nrow(AWQ_data_java))
FP_data_java <- FP_data_java[1:min_length_java, ]
AWQ_data_java <- AWQ_data_java[1:min_length_java, ]

print("********************** (HE) DeepseekCoder-1.3B FP vs AWQ Comparison (Python) *********************************")

# Initialize results list
res_py = list(Wilcoxon.p = c())

# Function to check if a column is constant
is_constant <- function(x) {
  return(length(unique(x)) == 1)
}

# Perform Wilcoxon tests
wilcox_test <- function(x, y) {
  if (is_constant(x) & is_constant(y)) {
    return(NA)
  }
  return(wilcox.test(x, y, alternative="two.side", paired=TRUE, exact=FALSE, correct=FALSE)$p.value)
}

print("Reliability - FP vs AWQ (Python)")
res_py$Wilcoxon.p = append(res_py$Wilcoxon.p, wilcox_test(FP_data_py$Reliability, AWQ_data_py$Reliability))
cliff.delta(FP_data_py$Reliability, AWQ_data_py$Reliability)

print("Maintainability - FP vs AWQ (Python)")
res_py$Wilcoxon.p = append(res_py$Wilcoxon.p, wilcox_test(FP_data_py$Maintainability, AWQ_data_py$Maintainability))
cliff.delta(FP_data_py$Maintainability, AWQ_data_py$Maintainability)

print("Security Hotspots - FP vs AWQ (Python)")
res_py$Wilcoxon.p = append(res_py$Wilcoxon.p, wilcox_test(FP_data_py$Security_Hotspots, AWQ_data_py$Security_Hotspots))
cliff.delta(FP_data_py$Security_Hotspots, AWQ_data_py$Security_Hotspots)

print("Cyclomatic Complexity (CyC) - FP vs AWQ (Python)")
res_py$Wilcoxon.p = append(res_py$Wilcoxon.p, wilcox_test(FP_data_py$CyC, AWQ_data_py$CyC))
cliff.delta(FP_data_py$CyC, AWQ_data_py$CyC)

print("Cognitive Complexity (CoC) - FP vs AWQ (Python)")
res_py$Wilcoxon.p = append(res_py$Wilcoxon.p, wilcox_test(FP_data_py$CoC, AWQ_data_py$CoC))
cliff.delta(FP_data_py$CoC, AWQ_data_py$CoC)

print("********************** (HE) DeepseekCoder-1.3B FP vs AWQ Comparison (Java) *********************************")

res_java = list(Wilcoxon.p = c())

print("Reliability - FP vs AWQ (Java)")
res_java$Wilcoxon.p = append(res_java$Wilcoxon.p, wilcox_test(FP_data_java$Reliability, AWQ_data_java$Reliability))
cliff.delta(FP_data_java$Reliability, AWQ_data_java$Reliability)

print("Maintainability - FP vs AWQ (Java)")
res_java$Wilcoxon.p = append(res_java$Wilcoxon.p, wilcox_test(FP_data_java$Maintainability, AWQ_data_java$Maintainability))
cliff.delta(FP_data_java$Maintainability, AWQ_data_java$Maintainability)

print("Security Hotspots - FP vs AWQ (Java)")
res_java$Wilcoxon.p = append(res_java$Wilcoxon.p, wilcox_test(FP_data_java$Security_Hotspots, AWQ_data_java$Security_Hotspots))
cliff.delta(FP_data_java$Security_Hotspots, AWQ_data_java$Security_Hotspots)

print("Cyclomatic Complexity (CyC) - FP vs AWQ (Java)")
res_java$Wilcoxon.p = append(res_java$Wilcoxon.p, wilcox_test(FP_data_java$CyC, AWQ_data_java$CyC))
cliff.delta(FP_data_java$CyC, AWQ_data_java$CyC)

print("Cognitive Complexity (CoC) - FP vs AWQ (Java)")
res_java$Wilcoxon.p = append(res_java$Wilcoxon.p, wilcox_test(FP_data_java$CoC, AWQ_data_java$CoC))
cliff.delta(FP_data_java$CoC, AWQ_data_java$CoC)

print("***************************************************************************")

# Create data frames without dropping NA values
res_df_py = data.frame(Wilcoxon.p = res_py$Wilcoxon.p)
res_df_py$Wilcoxon.p = p.adjust(res_df_py$Wilcoxon.p, method="holm")
print("Python Results:")
print(res_df_py)

res_df_java = data.frame(Wilcoxon.p = res_java$Wilcoxon.p)
res_df_java$Wilcoxon.p = p.adjust(res_df_java$Wilcoxon.p, method="holm")
print("Java Results:")
print(res_df_java)
