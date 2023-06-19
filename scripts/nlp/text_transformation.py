from processing import df_preprocessed
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

# Then, perform the TF-IDF transformation
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

# Apply the vectorizer
X = vectorizer.fit_transform(df_preprocessed['joined_tokens'])

# Get feature names (words/terms)
feature_names = vectorizer.get_feature_names_out()

# Create a DataFrame
tfidf_df = pd.DataFrame(X.toarray(), columns=feature_names)

# Print the DataFrame
print(tfidf_df)