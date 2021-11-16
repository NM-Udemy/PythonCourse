#02_numpy_matrix.p#

import numpy as np

print(np.inf) # 無限大
print(np.NINF) # マイナスの無限大
print(np.NAN) # 非数
print(np.NZERO) # 負の0
print(np.PZERO) # 正の0
print(np.e) # ネイピア数
print(np.pi)  # 円周率

# 行列

mat = np.arange(1, 10).reshape(3,3)
print(mat)
print(mat.T) # 転置行列

x = np.empty([3,3]) # 行列の初期化
print(x)

print(np.eye(5)) # 単位行列
print(np.identity(3))

print(np.eye(3,2))
print(np.eye(5,5,1))
print(np.eye(5,5,-2))

print(np.ones((3,3,5)))
print(np.zeros((3,3,2)))

print(np.full((3,3,3), fill_value=3))

x = np.tri(3,3, k=-1)
print(x)
mat = np.arange(1,26).reshape(5,5)
print(mat)
print(np.tril(mat, k=-1))
print(np.triu(mat, k=-1))
