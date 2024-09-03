
from agent import Agent
from setup import Setup
from env import NarmBanditsPlayGround

if __name__=='__main__':
    epsilon = 0.1
    episodes = 1000

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

    import matplotlib.pyplot as plt

    plt.plot(env.average_rewards)
    plt.xlabel('Plays')
    plt.ylabel('Average Reward')
    plt.title(f'N-Armed Bandit with ε={epsilon}')
    plt.show()