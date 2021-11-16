# 19_pandas_series.py

import pandas as pd
import numpy as np

sr1 = pd.Series(['A', 'B', 'C', 'D'])
print(sr1)
print(list(sr1))
print(tuple(sr1))

# インデックスを指定する
sr = pd.Series([23, 24, 22, 21],
    index = ['Taro', 'Jiro', 'Hanako', 'Yoshiko']
)
sr = pd.Series(
    {
        'Taro': 23,
        'Jiro': 24,
        'Hanako': 22,
        'Yoshiko': 21
    }
)
print(sr)

# append。値の追加
sr2 = pd.Series({'Saburo': 20})
sr = sr.append(sr2)

print(sr)

print(sr.values) # 値だけ取り出す
print(sr.index) # インデックスだけ取り出す
filter = sr>22
print(sr[filter]) # 22より大きいものだけ取り出す

sr.name = '年齢'
sr.index.name = '名前'
print(sr)

# numpy -> Series

sr1 = pd.Series(np.random.randint(0,10,10))
sr2 = pd.Series(np.random.randint(0,10,10))
print(sr1)
print(sr1.unique()) # 重複削除して返す
print(sr1.value_counts()) # ヒストグラム


print(sr1 * sr2)



###################


sr1 = pd.Series(['A', 'B', 'C', 'D'])
sr1[1:] = ['E', 'F', 'G']
print(sr1)

sr1 = sr1.drop(1)
print(sr1)

sr1.reset_index(drop=True, inplace=True) # インデックスの張り直し
print(sr1)

sr1 = pd.Series(np.random.randint(0,10,10))
print(sr1)
sr1[5] = pd.NA
print(sr1)

print(sr1[~sr1.isna()])

# 統計処理
print(sr1.count()) # 欠損値を除く数
print(sr1.mean()) # 平均値
print(sr1.max()) # 最大値
print(sr1.var()) # 分散
print(sr1.std()) # 標準偏差
print(sr1.quantile(0.8)) # 昇順に並べて80%地点の値
print(sr1.min())
print(sr1)
print(sr1.describe()) # いろんな要素を表示