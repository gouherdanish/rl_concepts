from abc import abstractmethod, ABC

from entities.agent import Agent
from entities.env import GridWorld

class Game(ABC):
    def __init__(self,agent:Agent,env:GridWorld) -> None:
        self.agent = agent
        self.env = env

    @abstractmethod
    def run(self):
        pass
