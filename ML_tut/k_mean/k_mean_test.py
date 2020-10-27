import numpy as np
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from K_mean import K_mean

#X, y = make_blobs(centers=4, n_samples=500, n_features=2, shuffle=True, random_state=42)
X, y = make_blobs(centers=4, n_samples=500, n_features=2, shuffle=True, random_state=40)
print(X.shape)
print(y.shape)
clusters = len(np.unique(y))
print(clusters)
k = K_mean(k=clusters, max_iter=150, plot_step =True)
y_pred = k.predict(X)

k.plot()