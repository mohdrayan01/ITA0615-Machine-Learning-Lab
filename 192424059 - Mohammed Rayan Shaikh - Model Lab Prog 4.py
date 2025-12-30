import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
X = np.array([[1], [2], [3], [8], [9], [10]])
gmm = GaussianMixture(n_components=2)
gmm.fit(X)
labels = gmm.predict(X)
print("Cluster labels:", labels)
plt.scatter(X, np.zeros_like(X), c=labels)
plt.title("EM Algorithm Clustering")
plt.show()
