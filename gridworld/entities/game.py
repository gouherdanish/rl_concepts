from entities.agent import Agent
from entities.env import GridWorld

class Game:
    def __init__(self,agent:Agent,env:GridWorld) -> None:
        self.agent = agent
        self.env = env

    def run(self,episodes=500):
        for episode in range(episodes):
            print(f"<<<<< EPISODE {episode+1} START >>>>>")
            state = self.env.reset()
            action = self.agent.select_action(state)
            print(state,action)
            done = False
            i = 0
            while not done :
                # print([(s,a,q) for (s,a), q in self.agent.estimates.items() if q.value != 0])
                next_state, reward, done = self.env.step(state,action)
                next_action = self.agent.select_action(next_state)
                sarsa = (state,action.action,reward,next_state,next_action.action)
                print(sarsa)
                self.agent.update_estimates(*sarsa)
                state = next_state
                action = next_action
                i += 1
                if i > 100: done= True
                print([(s,a,q) for (s,a), q in self.agent.estimates.items() if q.value != 0])
            print(f"<<<<< EPISODE {episode+1} END >>>>>")
