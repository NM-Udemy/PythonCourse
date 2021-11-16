# 24_scipy_hierarchy_clustering.py
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

df = pd.read_csv('science_library/countries_position.csv')
print(df.head(10))

longtitude_latitude = df.iloc[:,1:]
linked = linkage(longtitude_latitude, 'ward') # ウォード法

labels = list(df['country'])
print(labels)

dendrogram(linked, orientation='right', labels=labels)
plt.tight_layout()
plt.show()