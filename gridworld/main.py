from entities.agent import Agent
from entities.agent_params import AgentParams
from entities.env import GridWorld
from entities.game import Game

from constants import AgentParams, EnvParams

if __name__=='__main__':
    env = GridWorld(env_params=EnvParams())
    print(env)
    agent = Agent(states=env.states, agent_params=AgentParams())
    print(agent)

    game = Game(agent=agent,env=env)
    game.run(episodes=1)