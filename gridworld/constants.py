from enum import Enum

class AgentParams:
    ALPHA = 0.5         # learning rate
    GAMMA = 0.9         # discount factor
    EPSILON = 0.1       # greedy factor
    EPSILON_DECAY = 0.9

class EnvParams:
    GRID_SIZE = (2,2)               # grid size
    STEP_SIZE = 1                   # agent can step 1 cell up, down, left or right
    REWARD_POLICY = 'episodic'      # agent gets reward at the end of the episode
    GOAL_POS = (1,1)
    INITIAL_POS = (0,0)           

class Actions(Enum):
    RIGHT = 'right'
    DOWN = 'down'
    UP = 'up'
    LEFT = 'left'