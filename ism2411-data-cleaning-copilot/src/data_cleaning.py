import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def clean_column_names(df):
    df = df.copy()
    new_cols = []
    for col in df.columns:
        col2 = str(col).strip().lower()
        col2 = col2.replace(" ", "_")
        col2 = "".join(ch if (ch.isalnum() or ch == "_") else "_" for ch in col2)
        while "__" in col2:
            col2 = col2.replace("__", "_")
        col2 = col2.strip("_")
        new_cols.append(col2)
    df.columns = new_cols
    return df

def strip_whitespace_from_text_columns(df, text_cols):
    df = df.copy()
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace({"": np.nan, "nan": np.nan})
    return df

def handle_missing_values(df):
    df = df.copy()
    if 'qty' in df.columns:
        df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
        df = df[~df['qty'].isna()]
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        overall_median = df['price'].median(skipna=True)
        if 'prodname' in df.columns:
            medians = df.groupby('prodname')['price'].median()
            def fill_price(row):
                if pd.notna(row['price']):
                    return row['price']
                pname = row.get('prodname', None)
                if pname in medians and not pd.isna(medians[pname]):
                    return medians[pname]
                return overall_median
            df['price'] = df.apply(fill_price, axis=1)
        else:
            df['price'] = df['price'].fillna(overall_median)
    return df

def remove_invalid_rows(df):
    df = df.copy()
    if 'qty' in df.columns:
        df['qty'] = pd.to_numeric(df['qty'], errors='coerce')
        df = df[df['qty'] >= 0]
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df = df[df['price'] >= 0]
    return df

def run_cleaning_pipeline(raw_path):
    df_raw = load_data(raw_path)
    df = clean_column_names(df_raw)
    df = strip_whitespace_from_text_columns(df, ['prodname','category'])
    df = handle_missing_values(df)
    df = remove_invalid_rows(df)
    return df

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"
    df_clean = run_cleaning_pipeline(raw_path)
    df_clean.to_csv(cleaned_path, index=False)
    print(df_clean.head())
