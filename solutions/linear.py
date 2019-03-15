import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_blobs
from matplotlib.colors import ListedColormap

X, y = make_blobs(n_samples=400, centers=2, cluster_std=1., random_state=0)

# train the linear regressor and save the coefficents

reg = linear_model.LinearRegression()
reg.fit(X, y)
b_1, b_2 = reg.coef_
b_0 = reg.intercept_

# solve the function y = b_0 + b_1*X_1 + b_2 * X_2 for X2
x1s = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]), 2)
x2s = (0.5 - b_0 - b_1 * x1s) / b_2


fig, ax = plt.subplots()

ax.scatter(X[:, 0], X[:, 1], s=25, c=y, cmap=ListedColormap(['C0', 'C1']))

ax.plot(x1s, x2s, color='gray', linestyle='--')

ax.grid()
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.margins(x=0, y=0)

ax.fill_between(x1s, x2s, np.max(X[:, 1]), color='C0', alpha=0.1)
ax.fill_between(x1s, x2s, np.min(X[:, 1]), color='C1', alpha=0.1)
ax.set_aspect(1)
