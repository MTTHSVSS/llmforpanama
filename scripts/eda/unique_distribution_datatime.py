import pandas as pd

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