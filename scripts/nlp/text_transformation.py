from feature_extraction import df_bow

# Join tokens into string
df['text'] = df_bow['tokens'].apply(' '.join)

print(df)