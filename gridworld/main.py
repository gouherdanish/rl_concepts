from entities.agent import Agent
from entities.env import GridWorld
from entities.game import Game

from constants import AgentParams, EnvParams

if __name__=='__main__':
    env = GridWorld(env_params=EnvParams())
    agent = Agent(states=env.states, agent_params=AgentParams())
    game = Game(agent=agent,env=env)
    game.run(episodes=3)