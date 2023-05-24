import os
import pandas as pd

# Get the file names in the data/raw directory
file_names = os.listdir('/workspaces/llmforpanama/data/raw')

for file_name in file_names:
    if file_name.endswith('.csv'):
        file_path = os.path.join('/workspaces/llmforpanama/data/raw', file_name)
        df = pd.read_csv(file_path)
        
        # Identify missing values in the DataFrame
        missing_values = df.isnull().sum()
        
        # Print the number of missing values for each column
        print(f"Missing values in {file_name}:")
        print(missing_values)
        print()