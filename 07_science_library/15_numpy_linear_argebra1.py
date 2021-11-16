# 15_numpy_linear_argebra1.py

import numpy as np

print(np.dot(8,5))

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[9,3]])

print(a)
print(b)
print(np.dot(a,b)) # 内積

a = np.random.rand(10,5)
b = np.random.rand(5,2)
c = np.random.rand(2,3)
d = np.random.rand(3,4)

e = np.linalg.multi_dot([a,b,c,d]) # いっぺんに内積をとる
print(e)

d = np.array([1,2,3])
e = np.array([4,5,6])
print(np.inner(d,e))
print(np.outer(d,e))
print(np.cross(d,e)) # 2*6 - 3*5 = -3, 3*4-1*6=6
