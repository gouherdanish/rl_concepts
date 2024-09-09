from entities.agent import Agent
from entities.agent_params import AgentParams
from entities.env import GridWorld
from entities.setup import Setup

from constants import Params

if __name__=='__main__':
    env = GridWorld()

    agent_params = AgentParams(
        epsilon=Params.EPSILON,
        alpha=Params.ALPHA,
        gamma=Params.GAMMA)
    
    agent = Agent(
        states=env.states, 
        params=agent_params 
    )
