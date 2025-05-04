# scripts/05_evaluation.py
# Pseudocode:
#   – import pandas, sklearn.metrics, joblib, os
#   – load model and test split
#   – predict on X_test
#   – compute MAE, RMSE, R²
#   – save metrics to outputs/evaluation/metrics.txt
#   – plot actual vs predicted and residuals
#   – save plots to outputs/figures/evaluation/
