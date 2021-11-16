#18_numpy_approximation.p#

import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(100) * 2 - 1
noise = np.random.rand(100) * 5

y = x*2 + noise

a, b = np.polyfit(x,y,1)

plt.scatter(x,y)

print(np.corrcoef(x,y))

test_x = np.linspace(np.min(x), np.max(x), 100)
test_y = a * test_x  + b
plt.plot(test_x, test_y)
plt.show()

x = np.random.rand(100) * 2 - 1
noise = np.random.rand(100)
y = x**3 - 0.25*x**2 + noise
plt.scatter(x,y)
a,b,c,d = np.polyfit(x,y,3)

test_x = np.linspace(np.min(x), np.max(x), 100)
# test_y = a* test_x **3 + b * test_x **2 + c * test_x + d
# plt.plot(test_x, test_y)
# plt.show()


func = np.poly1d(np.polyfit(x,y,3))

plt.plot(test_x, func(test_x))
plt.show()