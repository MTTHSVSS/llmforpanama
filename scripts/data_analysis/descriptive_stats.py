# Import necessary libraries
import pandas as pd
import numpy as np

# Load your dataset
df = pd.read_csv('/workspaces/llmforpanama/data/raw/Officers.csv')

# Get the descriptive statistics
desc_stats = df.describe()

# Get the mode of the data
mode = df.mode

# Print the results
print("Descriptive Statistics:\n", desc_stats)
print("\nMode:\n", mode)