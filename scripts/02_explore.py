import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    os.makedirs('../outputs/eda', exist_ok=True)
    os.makedirs('../outputs/figures/eda', exist_ok=True)

    df = pd.read_csv('../outputs/processed/processed_permits.csv',
                     parse_dates=['IssuedDate', 'AppliedDate', 'CompletedDate'],
                     infer_datetime_format=True)

    # summary stats
    num_stats = df.select_dtypes(include='number').describe()
    cat_stats = {col: df[col].value_counts().head(10) for col in ['PermitType', 'Neighborhood'] if col in df}
    
    num_stats.to_csv('../outputs/eda/numeric_summary.csv')
    with open('../outputs/eda/categorical_summary.txt', 'w') as f:
        for k, v in cat_stats.items():
            f.write(f"=== {k} ===\n{v.to_string()}\n\n")

    # time series: monthly counts
    ts = df.set_index('IssuedDate').resample('M').size()
    ts.to_csv('../outputs/eda/monthly_counts.csv')

    # plots
    plt.figure()
    df['processing_time'] = (df['IssuedDate'] - df['AppliedDate']).dt.days
    df['processing_time'].hist(bins=50)
    plt.title('Processing Time Distribution (days)')
    plt.savefig('../outputs/figures/eda/processing_time_hist.png')
    plt.close()

    plt.figure()
    ts.plot()
    plt.title('Monthly Permit Counts')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.savefig('../outputs/figures/eda/monthly_permits.png')
    plt.close()

    print("EDA complete. Outputs in outputs/eda/ and outputs/figures/eda/")

if __name__ == '__main__':
    main()
