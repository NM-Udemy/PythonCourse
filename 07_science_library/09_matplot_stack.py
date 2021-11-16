# 09_matplot_stack.py

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y1 = x
y2 = 2*x
y3 = 3*x
plt.stackplot(x, y1, y2, y3, colors=['blue', 'green', 'yellow'])
plt.show()