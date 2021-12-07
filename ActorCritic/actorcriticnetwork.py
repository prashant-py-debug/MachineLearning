import tensorflow.keras as keras
from tensorflow.keras.layers import Dense
import os

class AC_network(keras.Model):
    def __init__(self,n_actions, fc1_dims = 1024 , fc2_dims = 512, model_name = "actor_critic" ,
     ckpt_dir="temp/actor_critic"):
        super(AC_network,self).__init__()
        self.n_actions = n_actions
        self.fc1_dims = fc1_dims
        self.fc2_dims = fc2_dims
        self.model_name = model_name
        self.ckpt_dir = ckpt_dir
        self.ckpt_file = os.path.join(self.ckpt_dir , model_name + "ac")

        self.fc1 = Dense(self.fc1_dims, activation='relu')
        self.fc2 = Dense(self.fc2_dims , activation="relu")
        self.v = Dense(1 )
        self.pi = Dense(self.n_actions,activation="softmax")

    def call(self,state):
        value = self.fc1(state)
        value = self.fc2(value)
        v = self.v(value)
        pi = self.pi(value)

        return v , pi


