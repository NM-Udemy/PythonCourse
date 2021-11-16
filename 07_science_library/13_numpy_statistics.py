#13_numpy_statistics.p#


import numpy as np

a = np.random.randint(0,10, 10)
print(a)
print(np.median(a)) # 中央値
print(np.mean(a)) # 平均値
print(np.std(a)) # 標準偏差
print(np.var(a)) # 分散

# 平均値
a = np.random.randint(0, 10, (2, 5))
print(a)
print(np.average(a, axis=0, weights=[1,10]))

# パーセンタイル(25%くらいの値、75％くらいの値)
a = np.random.rand(100)
lower, upper = np.percentile(a, [25, 75])
print(a[(a > lower) & (a < upper)])

# ヒストグラム
a = np.array([0,1,1,1,2,2,3,3,4,5,5,5,5,6,10])
print(np.histogram(a, bins=20))