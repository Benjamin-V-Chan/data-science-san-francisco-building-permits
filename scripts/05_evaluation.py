import os
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

def main():
    os.makedirs('../outputs/evaluation', exist_ok=True)
    os.makedirs('../outputs/figures/evaluation', exist_ok=True)

    data = joblib.load('../outputs/models/permit_time_model.joblib')
    model = data['model']
    X_test = data['X_test']
    y_test = data['y_test']

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)

    with open('../outputs/evaluation/metrics.txt', 'w') as f:
        f.write(f"MAE: {mae:.2f}\nRMSE: {rmse:.2f}\nR2: {r2:.3f}\n")

    # actual vs predicted
    plt.figure()
    plt.scatter(y_test, preds, alpha=0.3)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted Processing Time')
    plt.savefig('../outputs/figures/evaluation/actual_vs_predicted.png')
    plt.close()

    # residuals
    plt.figure()
    plt.hist(y_test - preds, bins=50)
    plt.title('Residuals Distribution')
    plt.savefig('../outputs/figures/evaluation/residuals.png')
    plt.close()

    print("Evaluation complete. Metrics and plots saved.")

if __name__ == '__main__':
    main()
