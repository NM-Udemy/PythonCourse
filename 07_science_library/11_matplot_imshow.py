# 11_matplot_imshow.py

import matplotlib.pyplot as plt
import numpy as np

z = np.array([[2,2,3,4], [3,4,2,1], [1,2,3,4]])
z = np.random.rand(100, 100)

plt.imshow(z, origin='lower')
plt.colorbar()
plt.show()

import matplotlib.image as mpimg

img = mpimg.imread('test.jpg')
print(img)
plt.imshow(img)
plt.show()

