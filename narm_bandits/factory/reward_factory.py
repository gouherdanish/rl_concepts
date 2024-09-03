from abc import abstractmethod, ABC
import numpy as np

from reward import Reward

class RewardFactory:
    registry = {}

    @classmethod
    def register(cls,type):
        def inner(wrapped_cls):
            cls.registry[type] = wrapped_cls
            return wrapped_cls
        return inner
    
    @classmethod
    def get(cls,type,**kwargs):
        return cls.registry[type](**kwargs)

class RewardDistribution(ABC):
    @abstractmethod
    def _select_reward(self):
        pass

    def select_reward(self):
        reward = self._select_reward()
        return Reward(value=reward)
    
@RewardFactory.register('constant')
class ConstantRewardDistribution(RewardDistribution):
    def __init__(self, reward_dist: np.array) -> None:
        self.reward_dist = reward_dist

    def __str__(self) -> str:
        return f'ConstantRewardDistribution({self.reward_dist})'
    
    def __repr__(self) -> str:
        return str(self)

    def _select_reward(self):
        return self.reward_dist[0]

@RewardFactory.register('random')
class RandomRewardDistribution(RewardDistribution):
    def __init__(self, reward_dist: np.array) -> None:
        self.reward_dist = reward_dist

    def __str__(self) -> str:
        return f'RandomRewardDistribution({self.reward_dist})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def _select_reward(self):
        return np.random.choice(self.reward_dist)
    
@RewardFactory.register('normal')
class NormalRewardDistribution(RewardDistribution):
    def __init__(self, mean=0, std=1) -> None:
        self.mean = mean
        self.std = std

    def __str__(self) -> str:
        return f'NormalRewardDistribution({self.mean},{self.std})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def _select_reward(self):
        return np.random.normal(loc=self.mean,scale=self.std)