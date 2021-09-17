import numpy as np
from tqdm import tqdm
import random

class DynaQ_plus:

    def __init__(self,lr,gamma,n_actions,n_obervations,bin_size=20,epsilon = 1,eps_dcy = 0.998,kappa = 0.001):
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.eps_dcy = eps_dcy
        self.n_actions = n_actions
        self.n_obervations = n_obervations
        self.bin_size = bin_size
        self.q_table = np.zeros([self.n_obervations,self.n_actions])
        self.Model = {}
        self.kappa = kappa
        self.tau = np.zeros((self.n_obervations,self.n_actions))

        

    def model(self,transitions):
        for transition in transitions:
            state,new_state,action,reward,done = transition
            state_action = (state,action)
            self.Model[state_action] = (reward,new_state,done)

    def q_planning(self,steps):

        for _ in range(steps):
            state_action = random.choice(list(self.Model.keys()))
            self.tau[state_action] += 1
            reward,new_state,done = self.Model[state_action]
            reward = reward + self.kappa * np.sqrt(self.tau[state_action])
            if not done:
                self.q_table[state_action] += self.lr * (reward + (self.gamma * np.max(self.q_table[new_state]) - 
                self.q_table[state_action]))
            else:
                self.q_table[state_action] += self.lr * (reward  - self.q_table[state_action])

            
            

    def training(self,state,env,steps):
        
        
        # discrete_state = self.get_discrete_state(state)
        # new_discrete_state = self.get_discrete_state(new_state)
        done = False
        rewards = 0
        memory = []
        while not done:
            action = self.e_greedy(state)
            new_state,reward,done,_ = env.step(action)
            self.q_table[state][action] += self.lr * (reward + (self.gamma * np.max(self.q_table[new_state]) - 
                self.q_table[state][action]))
            state = new_state
            memory.append((state,new_state,action,reward,done))
            rewards += reward 
        self.model(memory)
        self.q_planning(steps)

        return rewards



    def metrics(self):
        pass

    def e_greedy(self,state):
        # discrete_state= self.get_discrete_state(state)

        if np.random.random() > self.epsilon:
            action = np.argmax(self.q_table[state])
        else:
            action = np.random.randint(0,self.n_actions)
        return action

    def get_discrete_state(self,state):

        bins = np.array([
        np.linspace(-4.8, 4.8, self.bin_size),
        np.linspace(-4, 4, self.bin_size),
        np.linspace(-.418, .418, self.bin_size),
        np.linspace(-4, 4, self.bin_size)
        ])

        state_index = []
        for i in range(self.n_obervations):
            state_index.append(np.digitize(state[i],bins[i]) - 1)
        return tuple(state_index)
