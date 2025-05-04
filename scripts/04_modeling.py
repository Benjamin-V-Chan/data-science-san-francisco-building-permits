import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import joblib

def main():
    os.makedirs('../outputs/models', exist_ok=True)
    df = pd.read_csv('../outputs/features/features.csv')
    
    # drop rows with NaN target
    df = df.dropna(subset=['processing_time'])
    X = df.drop(columns=['processing_time', 'AppliedDate', 'IssuedDate', 'CompletedDate', 'PermitType', 'Neighborhood'], errors='ignore')
    y = df['processing_time']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('scale', StandardScaler()),
        ('model', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    pipeline.fit(X_train, y_train)
    joblib.dump({'model': pipeline, 'X_test': X_test, 'y_test': y_test}, '../outputs/models/permit_time_model.joblib')
    print("Model trained and saved to outputs/models/permit_time_model.joblib")

if __name__ == '__main__':
    main()
