# data-science-san-francisco-building-permits

## Project Overview

This project analyzes San Francisco building permit applications (2013–2018) to understand processing times, seasonal trends, and geographic distribution. It provides a modular pipeline for:

* Data cleaning and preprocessing
* Exploratory data analysis (EDA) with summary statistics and plots
* Feature engineering for modeling
* Predictive modeling of permit processing time
* Model evaluation and diagnostics
* Comprehensive visualizations for insights and reporting

---

## Folder Structure

```
project-root/
├── data/                       # Raw and reference datasets
│   ├── Building_Permits.csv    # Raw building permit data
│   └── dictionary.csv          # Column descriptions (optional)
├── scripts/                    # Modular analysis scripts
│   ├── 01_load_and_clean.py
│   ├── 02_explore.py
│   ├── 03_feature_engineering.py
│   ├── 04_modeling.py
│   ├── 05_evaluation.py
│   └── 06_visualization.py
├── outputs/                    # Generated outputs
│   ├── processed/              # Cleaned data files
│   ├── eda/                    # EDA tables and summaries
│   ├── features/               # Feature matrices
│   ├── models/                 # Trained model files
│   ├── evaluation/             # Evaluation metrics
│   └── figures/                # Plots and visualizations
└── requirements.txt            # Python dependencies
```
