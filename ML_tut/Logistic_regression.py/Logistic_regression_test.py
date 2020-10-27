import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from Logistic_regression import Logistic_regression
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

standard_scale = StandardScaler()
bc = datasets.load_breast_cancer()
X , y = bc.data , bc.target

print(X.shape)
print(y.shape)

X_train, X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state = 1234)
X_train = standard_scale.fit_transform(X_train)
X_test = standard_scale.transform(X_test)

regressor = Logistic_regression(lr = 0.001 , n_iters = 1000)
regressor.fit(X_train , y_train)
predictions = regressor.predict(X_test)

def accuracy( y_true , y_pred):
    acc = np.sum(y_true == y_pred)/len(y_true)
    return acc
print(accuracy(y_test , predictions))

