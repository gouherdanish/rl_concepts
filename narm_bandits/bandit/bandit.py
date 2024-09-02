from abc import abstractmethod

import numpy as np

class Bandit:
    def __init__(self,reward_dist) -> None:
        reward_dist = reward_dist

    def pull(self):
        return self.reward_dist.select_reward()