import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from processing import preprocess_data

# Use the function to get the preprocessed data
df = preprocess_data()

# Join the tokenized words back into a string
df['joined_tokens'] = df['tokens'].apply(' '.join)

# Create a Bag-of-Words representation
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['joined_tokens'])

# Print the feature names and the BoW representation
print(vectorizer.get_feature_names_out())
print(X.toarray())

# Convert this matrix back to a DataFrame with labeled columns
feature_names = vectorizer.get_feature_names_out()
df_bow = pd.DataFrame(data=X.toarray(), columns=feature_names)
print(df_bow.head())