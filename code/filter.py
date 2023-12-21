import pandas as pd
import random

df = pd.read_csv(
    'C:/Users/minhb/OneDrive/Documents/GitHub/CS418_STS_VN/stsvv/test.csv',
    engine='python',
    encoding='utf-8',
    sep='\t',
    names=['Sentence 1', 'Sentence 2', 'Total score'],
    index_col=False,
    keep_default_na=False
)
removal = ['`', '~', '!', '@', '#', '^', '&', '*', '(', ')', '_', '-', '=', '+', '[', ']', '{', '}', ';', ':', '"', '<',
           '>', '.', '/', '?', "'"]

df_modified = df.copy()
for each in removal:
    df_modified['Sentence 1'] = df_modified['Sentence 1'].str.replace(each, '')
    df_modified['Sentence 2'] = df_modified['Sentence 2'].str.replace(each, '')

# Assuming you've performed modifications and stored the result in df_modified
# Export the modified DataFrame to a CSV file
df_modified.to_csv('modified_data.csv', index=False, sep='\t')



