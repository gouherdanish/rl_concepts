import numpy as np

from bandit import GreedyBandit
from reward.reward_distribution import ConstantRewardDistribution, RandomRewardDistribution, NormalRewardDistribution

class NarmBandits:
    def __init__(self,*slots,**params) -> None:
        self.slots = slots
        self.n = len(self.slots)
        self.epsilon = params['epsilon']

    def run(episodes):
        for episode in range(episodes):
            pass


if __name__=='__main__':
    bandit_1 = GreedyBandit(reward=5)
    bandit_2 = [1,5,3,6]
    bandit_3 = np.random.normal(loc=3,scale=1)
    epsilon = 0.1
    episodes = 10

    rl = NarmBandits(slot1,slot2,slot3,epsilon=epsilon)
    rl.run(episodes=episodes)