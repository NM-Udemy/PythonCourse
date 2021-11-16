# 23_scipy_kmeans_clustering.py

import matplotlib.pyplot as plt
from numpy import vstack, array
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq

# データ生成
data = vstack((rand(150, 2), (rand(150,2) + array([0.5, 0.5])))) # 300行2列
# plt.scatter(data[:,0], data[:,1])
# plt.show()

# 2つに分類
centroids, distortion = kmeans(data, 2) # 2つに分類した際の重心と重心からの距離の平均値
print(centroids)
print(distortion)

# クラスに分類
codes, distances = vq(data, centroids)
print(codes)
# codesが0のものを散布図に表示
plt.scatter(data[(codes==0), 0], data[(codes==0), 1], label='クラスA')
# codesが1のものを散布図に表示
plt.scatter(data[(codes==1), 0], data[(codes==1), 1], label='クラスB')
plt.scatter(centroids[:,0], centroids[:,1], label='重心')
plt.legend()

new_values = rand(10,2) + array([0.25, 0.25])
new_codes, _ = vq(new_values, centroids)
for i, code in enumerate(new_codes):
    class_value = 'クラスA' if code==0 else 'クラスB'
    print('x: ' + str(new_values[i][0]) + ' y: ' + str(new_values[i][1])
    + ' : ' + class_value)

plt.show()
