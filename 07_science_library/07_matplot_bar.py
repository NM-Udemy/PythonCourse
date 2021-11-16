# 07_matplot_bar.py

import matplotlib.pyplot as plt
import numpy as np


men_means = [20,34,30,35,27]
women_means = [25, 32, 34, 20, 25]
labels = ['20代', '30代', '40代', '50代', '60代']

x = np.arange(len(labels))

width = 0.35

rect1 = plt.bar(x - width / 2, men_means, width, color='blue')
rect2 = plt.bar(x + width / 2, women_means, width)
plt.xticks(x, labels=labels)
plt.grid()
plt.ylabel('Score')
plt.title('Score by gender')
# plt.annotate('HELLO', xy=(1,10))

def autoLabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height), xy=(rect.get_x() + rect.get_width() / 2, height + 0.5), ha='center')

autoLabel(rect1)
autoLabel(rect2)
plt.tight_layout()
plt.show()