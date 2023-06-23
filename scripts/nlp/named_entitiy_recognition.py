import pandas as pd
import spacy
from processing import preprocess_data

# Load the Spacy model

nlp = spacy.load('en_core_web_sm')

# Load DataFrame

df = preprocess_data()

# Let's assume you have a column in your dataframe name 'text' that contains textual data
# We will apply the NER on this column

def named_entity_recognition(text):  # make sure to include 'text' as an argument to your function
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Apply NER to each row in the 'name' column

df['entities'] = df['name'].apply(named_entity_recognition)

# Print the first 10 rows of the DataFrame to see the results
print(df.head(10))