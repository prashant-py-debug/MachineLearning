import tensorflow as tf 
import numpy as np
from tensorflow.keras.optimizers import Adam
import tensorflow_probability as tfp
from actorcriticnetwork import AC_network

class Agent:
    def __init__(self,lr=0.0003, gamma=0.99 ,n_actions= 2 ):
        self.lr = lr
        self.gamma = gamma
        self.action_space = [i for i in range(n_actions)]
        self.action = None

        self.ActorCritic = AC_network(n_actions=n_actions)
        self.ActorCritic.compile(optimizer = Adam(lr= self.lr))

    def choose_action(self,observation):
        state = tf.convert_to_tensor([observation] , dtype=tf.float32)
        _ , probs = self.ActorCritic(state)

        action_prob = tfp.distributions.Categorical(probs=probs)
        action = action_prob.sample()
        self.action = action 

        return action.numpy()[0]

    def save_checkpoint(self):
        print("...Saving checkpoint...")
        self.ActorCritic.save_weights(self.ActorCritic.ckpt_file)

    def load_checkpoint(self):
        print("...loading checkpoint...")
        self.ActorCritic.load_weights(self.ActorCritic.ckpt_file)


    def learn(self,state, reward, state_, done):
        state = tf.convert_to_tensor([state],dtype=tf.float32)
        state_ = tf.convert_to_tensor([state_],dtype=tf.float32)
        reward = tf.convert_to_tensor(reward,dtype=tf.float32)

        with tf.GradientTape(persistent=True)  as tape:
            state_value , prob = self.ActorCritic(state)
            state_value_ , _ = self.ActorCritic(state_)
            state_value = tf.squeeze(state_value)
            state_value_ = tf.squeeze(state_value_)

            action_prob = tfp.distributions.Categorical(probs= prob)
            log_prob = action_prob.log_prob(self.action)

            delta = reward + self.gamma*state_value_*(1 - int(done)) - state_value
            actor_loss = -log_prob * delta
            critic_loss = delta**2
            total_loss = actor_loss + critic_loss

        gradient = tape.gradient(total_loss,self.ActorCritic.trainable_variables)
        self.ActorCritic.optimizer.apply_gradients(zip(gradient,self.ActorCritic.trainable_variables))




