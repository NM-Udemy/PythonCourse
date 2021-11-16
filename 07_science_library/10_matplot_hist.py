# 10_matplot_hist.py

import matplotlib.pyplot as plt
import numpy as np

# x = np.array([0,1,1,2,2,3,3,3,4])
x = np.random.randn(100)
plt.hist(x, bins=20)
plt.show()

# 2D
x = np.random.normal(3, 4, 10000)
y = np.random.normal(3, 4, 10000)

plt.hist2d(x, y, bins=100, cmap='plasma')
print(dir(plt.cm))
plt.colorbar()

plt.show()