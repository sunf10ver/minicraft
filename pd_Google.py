import pandas as pd 

df = pd.read_csv('GoogleApps.csv')

print(df.info())
print(df.head())
print(df['Price'].sum())
print(df['Price'].max())
print(df['Price'].min())
categoryDf = df.groupby('Category').agg({'Rating': 'max', 'Rating': 'sum', 'Rating': 'min'})
print(categoryDf)
print(df['Category'])