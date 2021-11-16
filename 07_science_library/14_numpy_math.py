# 14_numpy_math.py


import numpy as np
import matplotlib.pyplot as plt


low = -np.pi
high = np.pi

N = 50

x = np.linspace(low, high, N)
y = np.sin(x)
plt.plot(x, y)
y = np.cos(x)
plt.plot(x, y)
y = np.tan(x)
plt.plot(x, y)
plt.ylim([-10,10])
plt.show()

x = np.linspace(1,10,N)
y = np.log(x) # logeX
plt.plot(x, y)

y = np.log10(x) # log10X
plt.plot(x, y)
plt.show()


x = np.arange(10)
y = np.exp(x) # eのx乗
y = np.exp2(x) # 2のx乗

plt.plot(x,y, 'o--')
plt.show()