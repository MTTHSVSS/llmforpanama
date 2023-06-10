import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# specify your filename
filename = "/workspaces/llmforpanama/data/raw/Entities.csv"

# Load the data into a DataFrame
df_entities = pd.read_csv ('/workspaces/llmforpanama/data/raw/Entities.csv')

# Convert date columns to datetime
df_entities['incorporation_date'] = pd.to_datetime(df_entities['incorporation_date'], errors='coerce')
df_entities['inactivation_date'] = pd.to_datetime(df_entities['inactivation_date'], errors='coerce')
df_entities['dorm_date'] = pd.to_datetime(df_entities['dorm_date'], errors='coerce')

# Count the number of unique entities
num_unique_entities = df_entities['name'].nunique()
num_unique_jurisdictions = df_entities['jurisdiction'].nunique()
num_unique_countries = df_entities['countries'].nunique()

# Explore the distribution of entities across different jurisdictions and countries.
jurisdiction_distribution = df_entities['jurisdiction'].value_counts()
country_distribution = df_entities['countries'].value_counts()
status_counts = df_entities['status'].value_counts()

# Get timeline information
incorporation_date_range = (df_entities['incorporation_date'].min(), df_entities['incorporation_date'].max())
inactivation_date_range = (df_entities['inactivation_date'].min(), df_entities['inactivation_date'].max())
dorm_date_range = (df_entities['dorm_date'].min(), df_entities['dorm_date'].max())

# Defined Output
print(f"Number of unique entities: {num_unique_entities}")
print("Number of unique jurisdictions: ", num_unique_jurisdictions)
print("Number of unique countries: ", num_unique_countries)
print("Jurisdiction distribution: \n", jurisdiction_distribution)
print("Country distribution: \n", country_distribution)
print("Entity status distribution: \n", status_counts)
print(f"Incorporation Date Range: {incorporation_date_range[0]} to {incorporation_date_range[1]}")
print(f"Inactivation Date Range: {inactivation_date_range[0]} to {inactivation_date_range[1]}")
print(f"Dormancy Date Range: {dorm_date_range[0]} to {dorm_date_range[1]}")

# Filter the jurisdictions with a count of 10,000 or more
filtered_jurisdiction_distribution = jurisdiction_distribution[jurisdiction_distribution >= 10000]

# Plot the filtered distribution of jurisdictions
plt.figure(figsize=(10, 6))
filtered_jurisdiction_distribution.plot(kind='bar')
plt.title('Distribution of Jurisdictions with Count >= 10,000')
plt.xlabel('Jurisdiction')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.savefig('jurisdiction_distribution_barplot.png')  # Save the plot as a .png file
plt.show()

# Group data by jurisdiction and count the number of entities
grouped_jurisdiction = df_entities.groupby('jurisdiction').size()

# Convert to DataFrame for compatibility with pandas boxplot
grouped_df = grouped_jurisdiction.reset_index(name='count')

# Create a box plot
plt.figure(figsize=(10, 6))  # Optional: specify the size of the plot
grouped_df['count'].plot(kind='box')
plt.title('Boxplot of Entity Counts per Jurisdiction')
plt.ylabel('Count')
plt.savefig('jurisdiction_distribution_boxplot.png')  # Save the plot as a .png file
plt.show()

# Convert incoperation date to datetime format
df_entities['incorporation_date'] = pd.to_datetime(df_entities['incorporation_date'])

# Calculate the number of days since incorporation
df_entities['days_since_incorporation'] = (datetime.now() - df_entities['incorporation_date']).dt.days

# Fill NaN values with 0 before converting to integers
df_entities['days_since_incorporation'] = df_entities['days_since_incorporation'].fillna(0).astype(int)

# Make sure it's in integer format
df_entities['days_since_incorporation'] = df_entities['days_since_incorporation'].astype(int)

# Encoding 'status' to numerical values
df_entities['status_encoded'] = df_entities['status'].map({'Active': 1, 'Inactive': 0}) # Add more statuses as required

# Create scatter plot
plt.scatter(df_entities['days_since_incorporation'], df_entities['status_encoded'])
plt.xlabel('Number of Days Since Incorporation')
plt.ylabel('Status')
plt.title('Scatter Plot of Number of Days Since Incorporation vs Status')
plt.savefig('incorporation_date_scatterplot.png')
plt.show()

correlation = df_entities['days_since_incorporation'].corr(df_entities['status_encoded'])
print(f"The correlation between days_since_incorporation and status_encoded is {correlation}")