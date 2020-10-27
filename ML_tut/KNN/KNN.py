import numpy as np
from collections import Counter

def eucledean_dist(x1 , x2):
    return np.sqrt(np.sum((x1 - x2)**2))

class KNN:

    def __init__(self , k = 3):
        self.k = k

    def fit(self , X , y):
        self.X_train = X
        self.y_train = y
         
        
    def predict(self , X):

        predicted_label = [self._predict(x) for x in X]
        return np.array(predicted_label)
    
    def _predict(self , x):
        #compute distances
        distances = [eucledean_dist(x , x_train) for x_train in self.X_train]

        #get the k nearest samples , distance
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        #majority vote , most common label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
        



