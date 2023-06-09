import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


def preprocess_data():
    # Download necessary nltk data
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    df = pd.read_csv('/workspaces/llmforpanama/data/raw/Entities.csv', low_memory=False)

    # Select a small subset of data for this exercise
    subset_df = df.sample(n=1000)

    # Apply text normalization: convert to lowercase and remove punctuation
    subset_df['normalized'] = subset_df['name'].apply(lambda x: ''.join([char for char in str(x).lower() if char not in string.punctuation]))

    # Apply tokenization, stopswords removal, stemming and lemmatization
    subset_df['tokens'] = subset_df['normalized'].apply(nltk.word_tokenize)
    subset_df['filtered_tokens'] = subset_df['tokens'].apply(lambda tokens: [token for token in tokens if token not in stop_words])
    subset_df['stemmed'] = subset_df['filtered_tokens'].apply(lambda tokens: [stemmer.stem(token) for token in tokens])
    subset_df['lemmatized'] = subset_df['filtered_tokens'].apply(lambda tokens: [lemmatizer.lemmatize(token) for token in tokens])

    # Apply POS tagging
    subset_df['pos_tags'] = subset_df['tokens'].apply(nltk.pos_tag)

    # Return the dataframe
    return subset_df

# Call a function and assign it a value
df_preprocessed = preprocess_data()

# Join the tokenized words back into a string on the original DataFrame
df_preprocessed['joined_tokens'] = df_preprocessed['tokens'].apply(' '.join)