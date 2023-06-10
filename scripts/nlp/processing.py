import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download necessary nltk data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

df = pd.read_csv('/workspaces/llmforpanama/data/raw/Entities.csv')

# Select a small subset of data for this exercise
subset_df = df.sample(n=1000)

# Apply punctuation removal
subset_df['no_punctuation'] = subset_df['name'].apply(lambda x: ''.join([char for char in x if char not in string.punctuation]))

# Apply tokenization, stopswords removal, stemming and lemmatization
subset_df['tokens'] = subset_df['no_punctuation'].apply(nltk.word_tokenize)
subset_df['filtered_tokens'] = subset_df['tokens'].apply(lambda tokens: [token for token in tokens if token.lower() not in stop_words])
subset_df['stemmed'] = subset_df['filtered_tokens'].apply(lambda tokens: [stemmer.stem(token) for token in tokens])
subset_df['lemmatized'] = subset_df['filtered_tokens'].apply(lambda tokens: [lemmatizer.lemmatize(token) for token in tokens])

# Apply POS tagging
subset_df['pos_tags'] = subset_df['tokens'].apply(nltk.pos_tag)

# Print dataframe
print(subset_df)