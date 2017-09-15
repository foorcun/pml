import matplotlib.pyplot as plt
import numpy as np

# CALISMIYOR DF TANIMLI DEĞİL MİŞ

y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
X = df.iloc[0:100, [0, 2]].values
plt.scatter(X[:50, 0], X[:50, 1],
	color='red', marker='x', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1],
	color='blue', marker='o', label='versicolor')
plt.xlabel('petal length')
plt.ylabel('sepal length')
plt.legend(loc='upper left')
plt.show()
