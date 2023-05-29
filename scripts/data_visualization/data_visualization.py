import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Directory containing the csv files
dir_path = '/workspaces/llmforpanama/data/raw/'

# Loop over all files in the directory
for filename in os.listdir(dir_path):
    # Check if the file is a csv file
    if filename.endswith('.csv'):
        # Construct the full file path
        file_path = os.path.join(dir_path, filename)
        
        # Read the data
        df = pd.read_csv(file_path, low_memory=False)

        # Count the occurrences of each category in 'sourceID' column
        source_counts = df['sourceID'].value_counts()

        # Plot the counts
        plt.figure(figsize=(10,5))
        sns.barplot(x=source_counts.index, y=source_counts.values, palette="Blues_d")

        plt.title(f'Counts of Records by Source in {filename}')
        plt.xlabel('Source')
        plt.ylabel('Count')
        plt.xticks(rotation=90)

        # Save the plot, using the filename (without .csv) as part of the image filename
        plt.savefig(f'/workspaces/llmforpanama/scripts/data_visualization/plots/source_counts_{filename.replace(".csv", "")}.png')

        # Clear the figure to make room for the next one
        plt.clf()