# 03_numpy_manipulation

import numpy as np

x = np.arange(6)

print(x.reshape(2,3))
x = np.arange(8).reshape(2,4)
print(x)
print(np.ravel(x)) # 参照渡し
print(x.flatten()) # コピー渡し
y = np.ravel(x)
print(x)
y[0]=1000
print(x)

y = x.flatten('F')
print(y)

x = np.array([1,2,3])
y = np.array([4,5,6])

z = np.stack((x,y), axis=1)
print(z)

print(np.hstack((x,y))) # 横に結合
print(np.vstack((x,y))) # 縦方向
print(np.dstack((x,y))) # 深さ方向
print(np.dstack((x,y)).shape)

x = np.arange(9).reshape(3,3)
a, b, c = np.split(x, 3)

print(a, b, c)
a, b, c = np.hsplit(x, 3)

print(a)
print(b)
print(c)

x = np.arange(16).reshape(4,4)
print(x)
print(np.flip(x)) # 上下左右反転
print(np.flip(x, axis=0)) # 上下反転
print(np.flip(x, axis=1)) # 左右反転

print(x)
print(np.roll(x,5))
print(np.rot90(x,3)) # 90度反時計回り回転