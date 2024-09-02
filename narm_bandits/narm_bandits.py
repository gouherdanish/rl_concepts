import numpy as np

from agent import Agent
from setup import Setup

class NarmBandits:
    def __init__(self,agent,bandits) -> None:
        self.agent = agent
        self.bandits = bandits

    def run(self,episodes):
        for episode in range(episodes):
            print(f"Episode {episode} started...")
            action = self.agent.select_action()
            print(f"Action selected: {action}")
            bandit = self.bandits[action]
            print(f"Bandit selected: {bandit}")
            reward = bandit.pull_arm()
            agent.update_estimates(action,reward)


if __name__=='__main__':
    epsilon = 0
    episodes = 10

    setup = Setup()
    print(setup)

    agent = Agent(epsilon=epsilon)
    print(agent)

    rl = NarmBandits(agent,setup.bandits)
    rl.run(episodes=episodes)