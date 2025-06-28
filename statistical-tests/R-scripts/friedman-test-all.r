# === PYLINT Friedman Test ===
rm(list = ls())

metrics <- c("Error", "Warning", "Convention", "Refactor")
input_dir <- "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/prepared_friedman_pylint"
output_file <- "friedman_pylint_results.csv"

files <- list.files(input_dir, pattern = "*.csv", full.names = TRUE)
all_results <- data.frame()

for (metric in metrics) {
  metric_files <- files[grepl(metric, files)]

  for (f in metric_files) {
    df <- read.csv(f)
    if (ncol(df) < 3) next

    df_long <- reshape(df, direction = "long", varying = names(df)[-1], v.names = "value",
                       timevar = "generation", times = names(df)[-1], idvar = "TaskID")

    pval <- tryCatch({
      friedman.test(value ~ generation | TaskID, data = df_long)$p.value
    }, error = function(e) NA)

    result <- data.frame(model = gsub("_.*", "", basename(f)), metric = metric, p.value = pval)
    all_results <- rbind(all_results, result)
  }
}

all_results$signif <- ifelse(!is.na(all_results$p.value) & all_results$p.value < 0.01, "Yes", "No")
write.csv(all_results, output_file, row.names = FALSE)


# === FLAKE8 Friedman Test ===
rm(list = ls())

metrics <- c("ERROR", "WARNING", "PyFlakes")
input_dir <- "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/mceval-csv_pylint_pmd_flake8/prepared_friedman_flake8"
output_file <- "friedman_flake8_results.csv"

files <- list.files(input_dir, pattern = "*.csv", full.names = TRUE)
all_results <- data.frame()

for (metric in metrics) {
  metric_files <- files[grepl(metric, files)]

  for (f in metric_files) {
    df <- read.csv(f)
    if (ncol(df) < 3) next

    df_long <- reshape(df, direction = "long", varying = names(df)[-1], v.names = "value",
                       timevar = "generation", times = names(df)[-1], idvar = "TaskID")

    pval <- tryCatch({
      friedman.test(value ~ generation | TaskID, data = df_long)$p.value
    }, error = function(e) NA)

    result <- data.frame(model = gsub("_.*", "", basename(f)), metric = metric, p.value = pval)
    all_results <- rbind(all_results, result)
  }
}

all_results$signif <- ifelse(!is.na(all_results$p.value) & all_results$p.value < 0.01, "Yes", "No")
write.csv(all_results, output_file, row.names = FALSE)


# === SONARQUBE Friedman Test ===
rm(list = ls())

metrics <- c("Reliability", "Maintainability", "Security_Hotspots", "CyC", "CoC")
input_dir <- "/home/user/projects/NonFunc-AWQ/scripts/statistical-tests/csv-sonarqube-mceval/prepared_friedman_sonarqube-python"
output_file <- "friedman_sonarqube_results.csv"

files <- list.files(input_dir, pattern = "*.csv", full.names = TRUE)
all_results <- data.frame()

for (metric in metrics) {
  metric_files <- files[grepl(metric, files)]

  for (f in metric_files) {
    df <- read.csv(f)
    if (ncol(df) < 3) next

    df_long <- reshape(df, direction = "long", varying = names(df)[-1], v.names = "value",
                       timevar = "generation", times = names(df)[-1], idvar = "TaskID")

    pval <- tryCatch({
      friedman.test(value ~ generation | TaskID, data = df_long)$p.value
    }, error = function(e) NA)

    result <- data.frame(model = gsub("_.*", "", basename(f)), metric = metric, p.value = pval)
    all_results <- rbind(all_results, result)
  }
}

all_results$signif <- ifelse(!is.na(all_results$p.value) & all_results$p.value < 0.01, "Yes", "No")
write.csv(all_results, output_file, row.names = FALSE)
