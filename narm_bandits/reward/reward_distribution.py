from abc import abstractmethod
import numpy as np

from reward import Reward

class RewardDistribution:
    @abstractmethod
    def _select_reward(self):
        pass

    def select_reward(self):
        reward = self._select_reward()
        return Reward(value=reward)
    
class ConstantRewardDistribution(RewardDistribution):
    def __init__(self, reward_dist: np.array) -> None:
        self.reward_dist = reward_dist

    def _select_reward(self):
        return self.reward_dist[0]

class RandomRewardDistribution(RewardDistribution):
    def __init__(self, reward_dist: np.array) -> None:
        self.reward_dist = reward_dist

    def _select_reward(self):
        return np.random.choice(self.reward_dist)
    
class NormalRewardDistribution(RewardDistribution):
    def __init__(self, mean=0, std=1) -> None:
        self.mean = mean
        self.std = std

    def _select_reward(self):
        return np.random.normal(loc=self.mean,scale=self.std)