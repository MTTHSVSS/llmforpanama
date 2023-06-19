from processing import df_preprocessed
from sklearn.feature_extraction.text import CountVectorizer

# Then, perform the TF-IDF transformation
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

# Apply the vectorizer
X = vectorizer.fit_transform(df_preprocessed['joined_tokens'])