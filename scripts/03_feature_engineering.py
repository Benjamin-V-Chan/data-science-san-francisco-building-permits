import os
import pandas as pd

def main():
    os.makedirs('../outputs/features', exist_ok=True)
    df = pd.read_csv('../outputs/processed/processed_permits.csv',
                     parse_dates=['IssuedDate', 'AppliedDate'],
                     infer_datetime_format=True)

    df['year'] = df['IssuedDate'].dt.year
    df['month'] = df['IssuedDate'].dt.month
    df['weekday'] = df['IssuedDate'].dt.weekday

    df['processing_time'] = (df['IssuedDate'] - df['AppliedDate']).dt.days
    df['delayed'] = (df['processing_time'] > df['processing_time'].median()).astype(int)

    # one‐hot top permit types
    if 'PermitType' in df:
        top = df['PermitType'].value_counts().nlargest(10).index
        for t in top:
            df[f'pt_{t}'] = (df['PermitType'] == t).astype(int)
        df['pt_Other'] = (~df['PermitType'].isin(top)).astype(int)

    df.to_csv('../outputs/features/features.csv', index=False)
    print("Features saved to outputs/features/features.csv")

if __name__ == '__main__':
    main()
