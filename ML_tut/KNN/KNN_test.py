import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap = ListedColormap(["#FF0000" , "#00FF00" , "#0000FF"])

iris = datasets.load_iris()
X , y = iris.data , iris.target
print(len(X),len(y))

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state = 1234)

# print(X_train.shape)
# print(X_train[0])

# print(y_train.shape)
# print(y_train)

from KNN import KNN

clf = KNN(3)

clf.fit(X_train, y_train)

prediction = clf.predict(X_test)

acc = np.sum(prediction == y_test)/len(y_test)
print(acc)

# plt.figure()
# plt.scatter(X[:,1], X[:,2] , c=y , cmap=cmap , edgecolor="k" ,s = 20)
# plt.show()