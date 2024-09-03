import numpy as np

from agent import Agent
from setup import Setup

class NarmBanditsPlayGround:
    def __init__(self,agent,bandits) -> None:
        self.agent = agent
        self.bandits = bandits
        self.total_rewards = 0
        self.rewards = []

    def run(self,episodes):
        for _ in range(episodes):
            action = self.agent.select_action()
            bandit = self.bandits[action]
            reward = bandit.pull_arm()
            agent.update_estimates(action,reward)
            self.update(reward=reward)

    def update(self,reward):
        self.rewards.append(reward)
        self.total_rewards += reward.value


if __name__=='__main__':
    epsilon = 0.1
    episodes = 100

    setup = Setup()
    bandits = setup.bandits
    print(bandits)

    agent = Agent(epsilon=epsilon,n_actions=len(bandits))
    print(agent)

    env = NarmBanditsPlayGround(agent=agent,bandits=bandits)
    env.run(episodes=episodes)
    print(env.agent)
    print(env.rewards)
    print(env.total_rewards)