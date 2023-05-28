import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv('/workspaces/llmforpanama/data/raw/Officers.csv', low_memory=False)

# Count the occurrences of each category in 'sourceID' column
source_counts = df['sourceID'].value_counts()

# Plot the counts
plt.figure(figsize=(10,5))
sns.barplot(x=source_counts.index, y=source_counts.values, palette="Blues_d")

plt.title('Counts of Records by Source')
plt.xlabel('Source')
plt.ylabel('Count')
plt.xticks(rotation=90)

plt.savefig('/workspaces/llmforpanama/scripts/data_visualization/plots')