from entities.agent import Agent
from entities.env import GridWorld
from entities.setup import Setup
from constants import Params

if __name__=='__main__':
    env = GridWorld()
    agent = Agent(
        states=env.states,
        epsilon=Params.EPSILON,
        alpha=Params.ALPHA,
        gamma=Params.GAMMA    
    )
