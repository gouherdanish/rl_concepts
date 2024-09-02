from abc import abstractmethod

import numpy as np

class Bandit:
    def __init__(self,reward_dist) -> None:
        self.reward_dist = reward_dist

    def __str__(self) -> str:
        return f'Bandit({self.reward_dist})'
    
    def __repr__(self) -> str:
        return str(self)

    def pull_arm(self):
        return self.reward_dist.select_reward()