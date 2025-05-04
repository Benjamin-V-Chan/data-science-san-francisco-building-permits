import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    os.makedirs('../outputs/figures/summary', exist_ok=True)
    df = pd.read_csv('../outputs/processed/processed_permits.csv',
                     parse_dates=['IssuedDate'], infer_datetime_format=True)

    # Permits by neighborhood
    if 'Neighborhood' in df.columns:
        counts = df['Neighborhood'].value_counts().head(10)
        plt.figure()
        counts.plot.barh()
        plt.title('Top 10 Neighborhoods by Permit Count')
        plt.xlabel('Count')
        plt.savefig('../outputs/figures/summary/permits_by_neighborhood.png')
        plt.close()

    # Permit types distribution
    if 'PermitType' in df.columns:
        pt = df['PermitType'].value_counts().head(10)
        plt.figure()
        pt.plot.pie(autopct='%1.1f%%')
        plt.title('Top 10 Permit Types')
        plt.ylabel('')
        plt.savefig('../outputs/figures/summary/permit_type_distribution.png')
        plt.close()

    # Seasonality heatmap of monthly counts
    df['year'] = df['IssuedDate'].dt.year
    df['month'] = df['IssuedDate'].dt.month
    pivot = df.pivot_table(index='month', columns='year', values='PermitNumber', aggfunc='count')
    plt.figure()
    plt.imshow(pivot, aspect='auto')
    plt.colorbar(label='Count')
    plt.title('Monthly Permit Counts by Year')
    plt.ylabel('Month')
    plt.xlabel('Year')
    plt.savefig('../outputs/figures/summary/seasonality_heatmap.png')
    plt.close()

    print("Summary visualizations saved to outputs/figures/summary/")

if __name__ == '__main__':
    main()
