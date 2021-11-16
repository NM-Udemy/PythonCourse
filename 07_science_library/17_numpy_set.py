# 17_numpy_set.py


import numpy as np

data = np.array([6, 1,2,3,3,3,2,1,1,4,5])
print(np.unique(data))

data = np.array([[1,1,2],[3,2,2],[4,5,5]])
print(np.unique(data))

# in1d, intersect1d, setxor1d, union1d

arr1 = np.array([0,1,2,4,3])
arr2 = np.array([4,1])
print(np.in1d(arr1, arr2))
arr1 = np.array([0,1,1,3])
arr2 = np.array([1,2,2,3])

print(np.intersect1d(arr1, arr2)) # 両方に含まれている要素、重複削除、ソート
print(np.setdiff1d(arr1, arr2)) # arr1にあって、arr2にない要素
print(np.setxor1d(arr1, arr2)) # arr1, arr2のどちらかにある要素
print(np.union1d(arr1, arr2)) # arr1, arr2のユニオン,重複削除、ソート
