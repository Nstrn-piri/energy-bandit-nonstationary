import numpy as np

class NonStationaryEnergyBandit:
    def __init__(self):
         self.true_rewards_before = np.array([-3.0, 2.0, 4.0])
         self.true_rewards_after = np.array([4.0, 6.0, 1.0])
         self.step_count = 0

    def step(self , action):
        self.step_count +=1
        if self.step_count <= 500 :
            true_reward = self.true_rewards_before[action]
        else :
            true_reward = self.true_rewards_after[action]
        reward = np.random.normal(true_reward , 1)
        return reward

env = NonStationaryEnergyBandit()
   

