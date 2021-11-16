# 16_numpy_linear_argebra2.py

import numpy as np


a = np.array([[5,6],[3,4]])
print(a)
print(np.linalg.det(a)) # 行列式の計算

b = np.linalg.inv(a) # 逆行列

print(b)
print(b.dot(a))

a = np.array([[2,1,-3],[4,-2,1],[3,5,-2]])
b = np.array([-4,9,5])
# ax = b => x
x = np.linalg.solve(a,b)
print(f'{a=}')
print(f'{b=}')
print(f'{x=}')
print(a.dot(x))

a = np.random.rand(3,3)
q,r = np.linalg.qr(a)
print(f'{a=}')
print(f'{q=}')
print(f'{r=}')
