from entities.agent import Agent
from entities.agent_params import AgentParams
from entities.env import GridWorld
from entities.game import Game

from constants import AgentParams

if __name__=='__main__':
    env = GridWorld()

    agent = Agent(
        states=env.states, 
        params=AgentParams() 
    )

    game = Game(
        agent=agent,
        env=env
    )
    game.run(episodes=1)