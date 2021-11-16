# 06_matplot_scatter.py

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(100)
y1 = np.random.rand(100) - 0.5
x2 = np.random.rand(100)
y2 = np.random.rand(100) + 0.5

plt.scatter(x1, y1, s=100, c='red')
plt.scatter(x2, y2, s=100, c='blue', marker='*')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('散布図')
plt.show()

x = np.linspace(0, 10, 100) + np.random.rand(100)
y = np.linspace(0, 10, 100) + 5 * np.random.rand(100)
z = np.linspace(0, 10, 100)
plt.scatter(x, y, s=100, c=z, cmap='Blues')
plt.colorbar()
plt.show()


