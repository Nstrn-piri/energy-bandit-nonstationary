import numpy as np

class NonStationaryAgent:
    def __init__(self , n_action , alpha , epsilon):
        self.n_action = n_action
        self.alpha = alpha
        self.epsilon = epsilon
        self.q_value = np.zeros(n_action)
        self.action_counts = np.zeros(n_action)

    def select_action(self):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.n_action)
        else:
            return np.argmax(self.q_value)

    def update(self, action, reward):
        self.action_counts[action] += 1
        self.q_value[action] += (self.alpha * (reward - self.q_value[action]))        