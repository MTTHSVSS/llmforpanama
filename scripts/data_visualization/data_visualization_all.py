import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

# Directory containing the csv files
dir_path = '/workspaces/llmforpanama/data/raw/'

# Function to find the first unique identifier column
def find_unique_identifier(df):
    for col in df.columns:
        if df[col].is_unique:
            return col
    return None

# Get a list of all files in the directory
all_files = os.listdir(dir_path)

# Filter out non-csv files
csv_files = [file for file in all_files if file.endswith('.csv')]

# Sort the list to make sure the order is consistent (helps with debugging)
csv_files.sort()

# Select the first csv file
filename = csv_files[0]

# Construct the full file path
file_path = os.path.join(dir_path, filename)

# Read the data
df = pd.read_csv(file_path, low_memory=False)

# Find the first unique identifier column
unique_identifier = find_unique_identifier(df)

if unique_identifier is not None:
    # Count the occurrences of each category in the unique identifier column
    counts = df[unique_identifier].value_counts()

    # Plot the counts
    plt.figure(figsize=(10,5))
    sns.barplot(x=counts.index, y=counts.values, palette="Blues_d")

    plt.title(f'Counts of Records by {unique_identifier} in {filename}')
    plt.xlabel(unique_identifier)
    plt.ylabel('Count')
    plt.xticks(rotation=90)

    # Save the plot, using the filename (without .csv) as part of the image filename
    plt.savefig(f'/workspaces/llmforpanama/scripts/data_visualization/plots/counts_{unique_identifier}_{filename.replace(".csv", "")}.png')

    # Clear the figure to make room for the next one
    plt.clf()
else:
    print(f"No unique identifier found in {filename}.")