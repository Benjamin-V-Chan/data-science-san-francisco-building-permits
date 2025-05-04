# scripts/03_feature_engineering.py
# Pseudocode:
#   – import pandas, numpy, os
#   – load cleaned data
#   – create:
#       • ‘year’, ‘month’, ‘weekday’ from issue date
#       • ‘processing_time’ = IssuedDate – AppliedDate (in days)
#       • binary target: ‘delayed’ if processing_time > X days
#   – one-hot encode top N permit types; group others as ‘Other’
#   – save feature matrix to outputs/features/features.csv
