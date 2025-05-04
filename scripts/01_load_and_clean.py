# scripts/01_load_and_clean.py
# Pseudocode:
#   – import pandas, numpy, os
#   – load raw CSV from data/Building_Permits.csv
#   – try loading data/dictionary.csv (if present) for column descriptions
#   – inspect shape, dtypes, missing‐value counts
#   – drop duplicate rows
#   – parse date columns to datetime (e.g., ‘IssuedDate’, ‘AppliedDate’, ‘CompletedDate’)
#   – handle missing:
#       • numeric → fill with median
#       • categorical → fill with 'Unknown'
#       • dates → leave NaT or drop if critical
#   – save cleaned DataFrame to outputs/processed/processed_permits.csv
