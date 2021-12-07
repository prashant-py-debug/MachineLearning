import tensorflow.keras as keras
from tensorflow.keras.layers import Dense


class PolicyGradientNetwork(keras.Model):
    def __init__(self,n_actions,fc1_dim = 256,fc2_dim = 256):
        super(PolicyGradientNetwork,self).__init__()
        self.fc1_dim = fc1_dim
        self.fc2_dim = fc2_dim
        self.n_actions = n_actions

        self.fc1 = Dense(self.fc1_dim, activation = "relu" )
        self.fc2 = Dense(self.fc2_dim , activation = "relu")
        self.pi = Dense(self.n_actions,activation="softmax")

    def call(self,state):
        value = self.fc1(state)
        value = self.fc2(value)
        pi = self.pi(value)

        return pi 

