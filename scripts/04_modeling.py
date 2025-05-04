# scripts/04_modeling.py
# Pseudocode:
#   – import pandas, sklearn (Pipeline, train_test_split, StandardScaler, RandomForestRegressor), joblib, os
#   – load features and target from outputs/features/features.csv
#   – split into train/test
#   – build Pipeline([('scale',StandardScaler()),('model',RandomForestRegressor())])
#   – fit on train
#   – save model to outputs/models/permit_time_model.joblib
