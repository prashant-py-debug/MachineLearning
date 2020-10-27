import numpy as np

class Logistic_regression:

    def __init__(self, lr = 0.001 , n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.biases = None
    
    def fit(self, X , y):
        n_samples , n_features = X.shape
        self.weights = np.zeros(n_features)
        self.biases = 0

        for _ in range(self.n_iters):
            linear_model = np.dot(X , self.weights) + self.biases
            y_predicted = self.sigmoid(linear_model)

            dw = (1/n_samples) * np.dot(X.T,(y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)

            self.weights -= self.lr*dw
            self.biases -= self.lr*db

    def predict(self, X):

        linear_model = np.dot(X , self.weights) + self.biases
        y_predicted = self.sigmoid(linear_model)
        y_predicted_class = [ 1 if i > 0.5 else 0 for i in y_predicted]
        return(np.array(y_predicted_class))
            
    def sigmoid(self,x):
        y = 1/(1 + np.exp(-x))
        return y

    
