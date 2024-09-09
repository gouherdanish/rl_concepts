from entities.agent import Agent
from entities.env import GridWorld
from entities.setup import Setup
from constants import Constants

if __name__=='__main__':

    setup = Setup()
    agent = Agent(
        epsilon=Constants.epsilon,
        alpha=Constants.alpha,
        gamma=Constants.gamma    
    )
    env = GridWorld(
        
    )
