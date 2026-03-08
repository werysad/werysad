from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

x, y = make_blobs(n_samples=150, n_features=2, centers=3, random_state=0)
print(x)
print(y)
plt.scatter(x[:, 0], x[:, 1], c='blue', marker='o', s=50)
plt.grid()
plt.tight_layout()
plt.show()

# KMeans clustering
km = KMeans(n_clusters=3, init='k-means++', n_init=100, max_iter=1000, random_state=0)
y_km = km.fit_predict(x)
print(y_km)

plt.scatter(x[y_km == 0, 0], x[y_km == 0, 1], s=50, c='pink', marker='s', label='cluster 1')
plt.scatter(x[y_km == 1, 0], x[y_km == 1, 1], s=50, c='blue', marker='o', label='cluster 2')
plt.scatter(x[y_km == 2, 0], x[y_km == 2, 1], s=50, c='green', marker='^', label='cluster 3')
plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, marker='+', c='red', label='centroids')
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
print('distortion: %.2f' % km.inertia_)

distortions = []
for i in range(1, 8):
    km = KMeans(n_clusters=i, init='k-means++', n_init=10, max_iter=300, random_state=0)
    km.fit(x)
    distortions.append(km.inertia_)
plt.plot(range(1, 8), distortions, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.tight_layout()
plt.show()

#Dendogram

import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#hierarchical clustering using single linkage (minimum distance)
plt.figure(1,figsize = (16,8))
dendogram = sch.dendrogram(sch.linkage(x,method='single'))
plt.title('Dendogram' )
plt.xlabel('X')
plt.ylabel('Euclidean distance')
plt.show()

#hierarchical clustering using complete linkage (maximum distance)
plt.figure(1,figsize = (16,8))
dendogram = sch.dendrogram(sch.linkage(x,method='complete'))
plt.title('Dendogram')
plt.xlabel('X')
plt.ylabel('Euclidean distance')
plt.show()

#hierarchical clustering using average linkage (average distance)
plt.figure(1,figsize = (16,8))
dendogram = sch.dendrogram(sch.linkage(x,method='average'))
plt.title('Dendogram')
plt.xlabel('X')
plt.ylabel('Euclidean distance')
plt.show()