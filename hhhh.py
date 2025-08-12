import pandas as pd

df = pd.read_csv('hhh.csv', sep = ', ', encoding='utf-8')
print(df.info())
df.loc[len(df)] = {'name': 'саша', 'city':'владивосток', 'age': 67}
print(df['name'])
df = df.drop(index=3)
print(df['name'])
df.loc[1, 'name'] = 'иван'
print(df['name'])