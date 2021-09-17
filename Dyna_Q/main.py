import gym
from dynaQ_plus import DynaQ_plus
from dynaQ import DynaQ 
import numpy as np
from tqdm import tqdm 
import matplotlib.pyplot as plt 

plt.rcParams["figure.figsize"] = (10,8)

env = gym.make("FrozenLake-v0",is_slippery=False)   #is_slippery true for stochastic env
LEARNING_RATE = 0.1
MIN_LR = 0.001
MIN_EPS = 0.01
GAMMA = 0.95
EPISODES = 10_000
PLANNING_STEPS = 5
SHOW_EVERY = 1000
LEARNING_DCY = 0.01
n_actions = 4
n_observations = 16

agent = DynaQ(LEARNING_RATE,GAMMA,n_actions,n_observations)
ep_rewards = []
avg_rewards = []

for episode in tqdm(range(1,EPISODES+1)):
    state = env.reset()
    rewards = agent.training(state,env,PLANNING_STEPS)
    ep_rewards.append(rewards)
    agent.epsilon *= agent.eps_dcy
    agent.epsilon = max(agent.epsilon,MIN_EPS)
    if episode > 2000:
        agent.lr -= LEARNING_DCY
        agent.lr = max(agent.lr,MIN_LR)

    if episode % SHOW_EVERY == 0:
        avg_rewards.append(sum(ep_rewards[-SHOW_EVERY:])/SHOW_EVERY)
        print("episode:",episode,"average reward:",sum(ep_rewards[-SHOW_EVERY:])/SHOW_EVERY ,
            "max:",max(ep_rewards[-SHOW_EVERY:]) , "epsilon:",agent.epsilon)


plt.plot(np.linspace(0,10000,10),avg_rewards)
plt.xlabel("Episodes")
plt.ylabel("Average rewards per 1000 episodes")
plt.title("DynaQ agent on FrozenLake-v0")
plt.show()