import numpy as np

class SVM:

    def __init__(self, lr = 0.01 , lambda_value = 0.01 , n_iters = 1000):
        self.lr = lr
        self.lambda_value = lambda_value
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self , X , y):
        _ , n_features = X.shape
        y_ = np.where(y <= 0 , -1 , 1)

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            for idx , x_i in enumerate(X):
                condition = y_[idx] * ( (np.dot(x_i , self.weights) )- self.bias) >= 1
                if condition:
                    self.weights -= self.lr * (2*self.lambda_value*self.weights)
                else:
                    self.weights -= self.lr * (2 * self.lambda_value * self.weights - np.dot(x_i, y_[idx]))
                    self.bias -= self.lr * y_[idx] 

    def predict(self , x):
        approx = np.dot(x , self.weights) - self.bias
        return np.sign(approx)

    
