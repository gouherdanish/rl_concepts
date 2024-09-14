import sys
from entities.agent import Agent
from entities.env import GridWorld
from entities.game import Game

from constants import AgentParams, EnvParams
from factory.game_factory import GameFactory
from factory.agent_factory import AgentFactory

if __name__=='__main__':
    env = GridWorld(env_params=EnvParams())
    agent = AgentFactory.get(method=sys.args()[1],states=env.states, agent_params=AgentParams())
    game = GameFactory.get(method=sys.args()[1],env=env,agent=agent)
    game.run(episodes=3)