# 08_matplot_pie.py

import matplotlib.pyplot as plt
import numpy as np

generations = ['10代', '20代', '30代', '40代', '50代']
numbers = [20, 30, 35, 40, 20]
explode=(0,0.1,0,0.1,0)
def func_pct(pct, numbers):
    number = int(round(pct / 100 * np.sum(numbers)))
    return '{:.2f}%\n{}人'.format(pct, number)

colors = ['#ffeedd', 'red', 'blue', '#aa1133', 'yellow']
plt.pie(numbers, labels=generations, explode=explode, colors=colors, counterclock=False, startangle=90,
 autopct=lambda pct: func_pct(pct, numbers))
plt.legend(generations, title='年代', bbox_to_anchor=(1,1))
plt.show()