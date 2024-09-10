from enum import Enum

class AgentParams:
    EPSILON = 0.5       # greedy factor
    ALPHA = 0.5         # learning rate
    GAMMA = 0.9         # discount factor

class EnvParams:
    GRID_SIZE = (2,2)               # grid size
    STEP_SIZE = 1                   # agent can step 1 cell up, down, left or right
    REWARD_POLICY = 'episodic'      # agent gets reward at the end of the episode
    GOAL_POS = (2,2)
    INITIAL_POS = (0,0)           

class Actions(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'