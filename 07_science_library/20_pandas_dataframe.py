# 20_pandas_dataframe.py

import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2,3],[4,5,6]])
print(df)

df = pd.DataFrame([[1,2,3],[4,5,6]], columns=['A', 'B','c'], index=['index1', 'index2'])

print(df)

print(df.T)

df = pd.DataFrame(np.random.randint(0,10,9).reshape(3,3))

print(df)
print(df.head(1)) # 頭から1行
print(df.tail(1)) # 後ろから1行

print('-' * 20)

df = pd.DataFrame(
    [
        ['Taro', 21, 'Man', 175],
        ['Jiro', 20, 'Man', 160],
        ['Hanako', 19, 'Woman', 155],
        ['Yoshiko', 18, 'Woman', 160]
    ],

    columns=['名前', '年齢', '性別', '身長']
)

print(df['名前'])
print(df.名前)

print(df[['名前', '年齢']])

new_member = pd.DataFrame(
    [['Saburo', 17, 'Man', 180],], columns=df.columns
)
df = df.append(new_member) # メンバーを追加
df.reset_index(drop=True, inplace=True)
print(df)

# 列の追加
df['体重'] = np.random.randint(50,80,5)
df['BMI'] = df['体重'] / (df['身長'] * 0.01)**2

print(df)

print(df.to_numpy())

# 統計値
print(df.describe())

print(df.mean())
print(df.max())
print(df.min())
print(df.var())
print(df.std())
print(df.count())
print(df.quantile(0.8))