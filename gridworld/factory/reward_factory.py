from abc import abstractmethod, ABC
import numpy as np

from constants import EnvParams
from entities.reward import Reward

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
    def __init__(self, states) -> None:
        self.reward_dist = {state:(Reward(1) if state == EnvParams.GOAL_POS else Reward(0)) for state in states}

    def __str__(self) -> str:
        return f'EpisodicRewardPolicy({self.reward_dist})'
    
    def __repr__(self) -> str:
        return str(self)

    def select_reward(self,state):
        return self.reward_dist[state]
