from enum import Enum

class Params:
    EPSILON = 0.1       # greedy factor
    ALPHA = 0.5         # learning rate
    GAMMA = 0.9         # discount factor
    GRID_SIZE = (2,2)   # grid size

class Actions(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'