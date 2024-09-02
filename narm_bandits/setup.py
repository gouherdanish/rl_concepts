from bandit import Bandit
from factory.reward_factory import RewardFactory

import numpy as np

class Setup:
    def __init__(self) -> None:
        self.reward_dist_1 = RewardFactory.get('constant',reward_dist=np.array([2]))
        self.reward_dist_2 = RewardFactory.get('random',reward_dist=np.array([1,5,3,6]))
        self.reward_dist_3 = RewardFactory.get('normal',mean=3,std=1)
        self.bandit_1 = Bandit(reward_dist=self.reward_dist_1)
        self.bandit_2 = Bandit(reward_dist=self.reward_dist_2)
        self.bandit_3 = Bandit(reward_dist=self.reward_dist_3)
        self.bandits = (self.bandit_1,self.bandit_2,self.bandit_3)

    def __str__(self) -> str:
        return f'Setup({self.bandits})'