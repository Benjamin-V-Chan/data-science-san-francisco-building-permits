import os
import pandas as pd

def load_data():
    return pd.read_csv('../data/Building_Permits.csv', low_memory=False)

def load_dictionary():
    path = '../data/dictionary.csv'
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

def clean_df(df):
    df = df.drop_duplicates()
    
    # parse dates
    for col in ['AppliedDate', 'IssuedDate', 'CompletedDate']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
  
    # handle missing
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna('Unknown')
    return df

def main():
    os.makedirs('../outputs/processed', exist_ok=True)
    raw = load_data()
    _ = load_dictionary()  # optional
    
    cleaned = clean_df(raw)
    cleaned.to_csv('../outputs/processed/processed_permits.csv', index=False)
    print("Saved cleaned data to outputs/processed/processed_permits.csv")

if __name__ == '__main__':
    main()
