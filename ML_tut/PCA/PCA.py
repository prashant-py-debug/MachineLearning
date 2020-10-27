import numpy as np

class PCA:
    def __init__(self, n_components ):
        self.n_components = n_components
        self.components = None
        self.mean = None
    
    def fit(self , X):
        #mean
        self.mean = np.mean(X , axis = 0)
        X = X - self.mean

        #covariance matix , cov fucntion needs samples as columns
        cov = np.cov(X.T)

        #eign values and eignvector
        eignvalues , eignvectors = np.linalg.eig(cov)
        # -> eigenvector v = [:,i] column vector, transpose for easier calculations
        eignvectors = eignvectors.T
        
        #sorted eign values and vector
        idx = np.argsort(eignvalues)[::-1]
        eignvectors = eignvectors[idx]
        eignvalues = eignvalues[idx]

        #store k numbers of eignvectors
        self.components = eignvectors[0:self.n_components]

    def transform(self , X):
        #projected data
        X = X - self.mean
        return np.dot(X, self.components.T)
        
