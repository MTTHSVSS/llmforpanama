import pandas as pd

# Load the data into a DataFrame
df_entities = pd.read_csv('/workspaces/llmforpanama/data/raw/Entities.csv')

# This will give you the count of missing values in each column
missing_values = df_entities.isnull().sum()

# This will output your missing values as a percentage
missing_percentage = (df_entities.isnull().sum() / len(df_entities)) * 100

print(missing_values)
print (missing_percentage)