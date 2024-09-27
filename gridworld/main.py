from argparse import ArgumentParser

from entities.env import GridWorld
from constants import AgentParams, EnvParams
from factory.game_factory import GameFactory
from factory.agent_factory import AgentFactory

class RL_Pipeline:
    def run(method,episodes):
        env = GridWorld(env_params=EnvParams())
        agent = AgentFactory.get(type=method, states=env.states, agent_params=AgentParams())
        game = GameFactory.get(method=method,env=env,agent=agent)
        game.run(episodes=episodes)

if __name__=='__main__':
    # Parsing Arguments
    arg_parser = ArgumentParser(description='Welcome to the Awesome Game of Grid World !')
    arg_parser.add_argument('-m','--method', type=str, default='sarsa', help='Reinforcement Learning Method to use; Supported methods are `sarsa`, `qlearning` ')
    arg_parser.add_argument('-n','--episodes', type=int, default=5, help='Number of episodes to run for; Should be a positive integer')
    args = arg_parser.parse_args()
    # Running RL pipeline
    RL_Pipeline.run(**vars(args))
