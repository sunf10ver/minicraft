import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('hhh.csv', sep = ', ', encoding='utf-8')
# print(df.info())
# df.loc[len(df)] = {'name': 'саша', 'city':'владивосток', 'age': 67}
# print(df['name'])
# df = df.drop(index=3)
# print(df['name'])
# df.loc[1, 'name'] = 'иван'
# print(df['name'])
# df.to_csv('hhh.csv', index = False)
s1 = {
    'id': [1, 2, 3, 4],
    'name': ['Альвин', 'Эвен', 'Джонс', 'Король'],
    'age': [23, 22, 50, 55]
    }
s2 = {
    'country': ['Germany', 'Poland', 'Russia', 'Germany'],
    'city': ['GGG', 'FFF', 'Moscow', 'lll'],
    'money': [1, 100, 10000000, 10000000]
    }

df1 = pd.DataFrame(s1)
df2 = pd.DataFrame(s2)
df_c =pd.concat([df1, df2], axis=1)
print(df_c)
df_c.to_csv('hhhhh.csv', index = True, encoding='utf-8')

df_c['money'].value_counts(ascending=True).plot(kind = 'pie')
plt.show()