from constants import Params
from entities.grid import Grid
from entities.state import State

class GridWorld:
    def __init__(self) -> None:
        self.grid = Grid(size=Params.GRID_SIZE)
        self.states = [State(row,col) for row in self.grid.rows for col in self.grid.cols]
        self.current_state = State(0,0)
        self.goal_state = State(Params.GRID_SIZE-1,Params.GRID_SIZE-1)

    def reset(self):
        self.current_state = State(0,0)