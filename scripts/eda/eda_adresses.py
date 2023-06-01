import pandas as pd

# The path to your specific CSV file
file_path = '/workspaces/llmforpanama/data/raw/Addresses.csv'

# Read in a portion of the file to get the column names
df = pd.read_csv(file_path, nrows=5)

# Print out the column names
print(f'File: {file_path.split("/")[-1]}')
print('Columns:')
for column in df.columns:
    print(column)

# Show the first few rows of data
print('\nSample Data:')
print(df.head())