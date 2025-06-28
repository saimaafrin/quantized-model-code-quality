# quantized-model-code-quality
Is Quantization a Dealbreaker? Empirical Insights from Large Code Models

Replication Package:

This repository contains the replication package for our study on the impact of quantization on Large Code Models (LCMs), focusing on code quality and static properties beyond functional correctness. Our investigation examines whether reducing model precision via Activation-Aware Weight Quantization (AWQ) affects key software engineering attributes such as maintainability, security, and structural complexity.
We evaluated quantized and full-precision LCMs using state-of-the-art static analysis tools, including SonarCloud, PMD, Pylint, and Flake8, across two programming languages (Python and Java) and two benchmarks (MultipLE and McEval). The replication package includes all relevant scripts, datasets, and documentation necessary to reproduce our experiments and extend our analysis.

Repository Structure
```
.
├── LICENSE
├── README.md
├── SonarCloud.pdf
├── generated-code-analysis
└── analysis-scripts
    ├── analysis_PMD_checkstyle.py
    ├── analysis_pylint_flake8.py
    ├── json-java.py
    └── json-python.py
```

# Project Repository Overview

This repository contains analysis scripts and resources for code generation tasks performed using the [MultipL-E](https://github.com/nuprl/MultiPL-E) repository. It also provides scripts for processing generated files, running code quality analyses with PMD, Checkstyle, Pylint, and Flake8, and instructions for integrating SonarCloud analysis.

---

## Installation

To install all necessary Python dependencies, use:

```bash
pip install -r requirements.txt
```

---

## Code Generation

- Generate your code using the [MultipL-E](https://github.com/nuprl/MultiPL-E) repository.
- After generation, you will receive `.gz` compressed files.
- Extract these files using the following command:

```bash
gunzip <your-generated-file>.gz
```

---

## JSON Extraction

Move into the `analysis-scripts` directory to convert the extracted JSON files to a readable format. Edit the directory path in the scripts and then run:

- For Python-generated code, run:

```bash
python json-python.py
```

- For Java-generated code, run:

```bash
python json-java.py
```

---

## Code Analysis

While in the `analysis-scripts` directory, perform analyses using:

- **Java Code Analysis (PMD & Checkstyle)**:

```bash
python analysis_PMD_checkstyle.py
```

- **Python Code Analysis (Pylint & Flake8)**:

```bash
python analysis_pylint_flake8.py
```

Check analysis results from the generated JSON and CSV files.

---

## SonarCloud Analysis

Follow the instructions detailed in [SonarCloud.pdf](SonarCloud.pdf) for integrating and conducting SonarCloud analyses.

## Our Generated code and Analysis reports
The `generated-code-analysis` directory contains the genarted code and the static tool's analysis reports. 



