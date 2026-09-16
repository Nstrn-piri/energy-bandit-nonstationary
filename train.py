import numpy as np
from environment import NonStationaryEnergyBandit
from agent import NonStationaryAgent
from plots import (
    plot_q_values,
    plot_cumulative_reward,
    plot_action_counts
)

np.random.seed(42)
env = NonStationaryEnergyBandit()
agent = NonStationaryAgent(n_action=3 , alpha=0.1 , epsilon=0.1)

rewards= []
actions = []
q_history = []

for step in range(1000):
    action = agent.select_action()
    reward = env.step(action)
    agent.update(action , reward)
    rewards.append(reward)
    actions.append(reward)
    q_history.append(agent.q_value.copy())

q_history = np.array(q_history)
cumulative_reward = np.cumsum(rewards)

print("Final Q values:")
print(agent.q_value)

print("\nAction counts:")
print(agent.action_counts)

print("\nAverage reward:")
print(np.mean(rewards))


plot_q_values(q_history)
plot_cumulative_reward(rewards)
plot_action_counts(agent.action_counts)