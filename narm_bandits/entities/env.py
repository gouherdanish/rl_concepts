
class NarmBanditsPlayGround:
    def __init__(self,agent,bandits) -> None:
        self.agent = agent
        self.bandits = bandits
        self.total_rewards = 0
        self.rewards = []
        self.average_rewards = []

    def run(self,episodes):
        for episode in range(1,episodes+1):
            action = self.agent.select_action()
            bandit = self.bandits[action]
            reward = bandit.pull_arm()
            self.agent.update_estimates(action,reward)
            self.update(reward=reward,episode=episode)

    def update(self,reward,episode):
        self.rewards.append(reward)
        self.total_rewards += reward.value
        self.average_rewards.append(self.total_rewards/episode)

