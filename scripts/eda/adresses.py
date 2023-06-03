import pandas as pd

# specify your filename
filename = "/workspaces/llmforpanama/data/raw/Addresses.csv"

# Comment out the parts of the script that you don't want to run
# df = pd.read_csv(filename, nrows=5)

# print(f"File: {filename.split('/')[-1]}")
# print("Columns:")
# print("\n".join(df.columns))

# print("\nSample Data:")
# print(df)

# count the lines in the file
num_lines = sum(1 for row in open(filename, 'r'))

print(f"\nNumber of rows (including header): {num_lines}")
print(f"Number of rows (excluding header): {num_lines - 1}")