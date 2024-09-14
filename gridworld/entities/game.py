from entities.agent import Agent
from entities.env import GridWorld

class Game:
    def __init__(self,agent:Agent,env:GridWorld) -> None:
        self.agent = agent
        self.env = env

