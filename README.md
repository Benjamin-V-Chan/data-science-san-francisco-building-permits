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

---

## Usage

1. **Setup the Project:**

   * Clone the repository.
   * Ensure you have Python installed.
   * Install required dependencies using the requirements.txt file.

     ```bash
     pip install -r requirements.txt
     ```

2. **Clean and Preprocess Data:**

   ```bash
   python3 scripts/01_load_and_clean.py
   ```

3. **Exploratory Data Analysis:**

   ```bash
   python3 scripts/02_explore.py
   ```

4. **Feature Engineering:**

   ```bash
   python3 scripts/03_feature_engineering.py
   ```

5. **Train Predictive Model:**

   ```bash
   python3 scripts/04_modeling.py
   ```

6. **Evaluate Model Performance:**

   ```bash
   python3 scripts/05_evaluation.py
   ```

7. **Generate Summary Visualizations:**

   ```bash
   python3 scripts/06_visualization.py
   ```

---

## Requirements

All dependencies are listed in `requirements.txt`. Major packages include:

* pandas
* numpy
* scikit-learn
* matplotlib
* joblib

---

## Acknowledgments

* **dataset name:** San Francisco Building Permits
* **dataset author:** Aparna Shastry
* **dataset source:** [https://www.kaggle.com/datasets/aparnashastry/building-permit-applications-data](https://www.kaggle.com/datasets/aparnashastry/building-permit-applications-data)
