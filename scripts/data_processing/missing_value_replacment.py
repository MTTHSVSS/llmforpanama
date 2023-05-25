import pandas as pd
import numpy as np

def fill_missing_values(df):
    # For numerical columns
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col].fillna(-999, inplace=True)

    # For object (including string) columns
    for col in df.select_dtypes(include=[object]).columns:
        df[col].fillna('Unknown', inplace=True)

    return df

def main():
    # Load your data
    df = pd.read_csv('your_data_file.csv')

    # Fill missing values
    df = fill_missing_values(df)

    # Save the cleaned data
    df.to_csv('cleaned_data.csv', index=False)

if __name__ == "__main__":
    main()
