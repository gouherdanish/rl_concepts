from abc import ABC, abstractmethod

from constants import Params, Actions
from entities.grid import Grid
from entities.state import State


class Env(ABC):
    def __init__(self) -> None:
        self.grid = Grid(size=Params.GRID_SIZE)
        self.states = [State(row,col) for row in self.grid.rows for col in self.grid.cols]
        self.current_state = State(0,0)
        self.goal_state = State(Params.GRID_SIZE-1,Params.GRID_SIZE-1)

    def reset(self):
        return State(0,0)

    @abstractmethod
    def step(self):
        pass

class GridWorld(Env):

    def step(self,state,action):
        next_state = State()
