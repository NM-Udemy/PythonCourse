# 21_pandas_readfile.py

import pandas as pd

df = pd.read_csv('science_library/people.csv') # delimiter: , escape: "
# delimiter = '\t'
# read_excel

print(df.head(3))
print(df.tail(3))

print(df.columns)

print(df[['first_name', 'last_name']][0:5])

# iloc 
print(df.iloc[1:4,5:10]) # 2-4行目, 6-11列目

# loc
pd.set_option('display.max_columns', None)
print(df.loc[df['first_name'] == 'Michael'])
df.loc[df['first_name'] == 'Michael'].\
    to_csv('science_library/output.csv', index=False, sep='\t')

print(df.sort_values(['first_name', 'last_name'], ascending=[1, 0]).\
    head(20)[['first_name', 'last_name']])

# 集計
print(df.describe())
print(df.age.sum())
print(df.age.min())
print(df.age.agg(['sum', 'max', 'mean']))

# 絞り込み

print(df.head(5))
print(df.loc[df['first_name'].str.contains('Mi')]) # MIを含むか
print(df.loc[~df['first_name'].str.contains('Mi')]) # MIを含まないか


print('-' * 100)

print(df.loc[df['first_name'].str.contains('William|Richard')])
print(df.loc[df['first_name'].str.contains('^A[a-z]*')])
print(df.loc[df['first_name'].str.contains('^A[a-z]*a$')])


df.loc[df['country'] == 'Japan', 'nationality'] = 'Japanese'
print(df.loc[df['country'] == 'Japan'])
print(df.head(3))

# group by

print(df.groupby(['country']).mean().sort_values('age'))

