from abc import abstractmethod, ABC
import numpy as np

from constants import EnvParams
from entities.reward import Reward
from entities.state import State

class RewardFactory:
    registry = {}

    @classmethod
    def register_policy(cls,type):
        def inner(wrapped_cls):
            cls.registry[type] = wrapped_cls
            return wrapped_cls
        return inner
    
    @classmethod
    def get_policy(cls,type,**kwargs):
        return cls.registry[type](**kwargs)

class RewardPolicy(ABC):
    @abstractmethod
    def select_reward(self):
        pass
    
@RewardFactory.register_policy('episodic')
class EpisodicRewardPolicy(RewardPolicy):
    def __str__(self) -> str:
        return f'EpisodicRewardPolicy()'
    
    def __repr__(self) -> str:
        return str(self)

    def select_reward(self,done):
        return 1 if done else 0
