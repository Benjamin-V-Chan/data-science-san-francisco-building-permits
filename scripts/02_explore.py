# scripts/02_explore.py
# Pseudocode:
#   – import pandas, matplotlib.pyplot, os
#   – load cleaned data from outputs/processed/processed_permits.csv
#   – compute summary statistics:
#       • numeric.describe()
#       • value_counts() for key categorical fields
#   – compute time‐series of permits per month
#   – save stats to outputs/eda/summary_stats.csv
#   – plot:
#       • histogram of processing time
#       • line chart of monthly permit counts
#   – save plots to outputs/figures/eda/
