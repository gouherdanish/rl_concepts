from abc import ABC, abstractmethod

from constants import EnvParams
from entities.grid import Grid
from entities.state import State
from factory.action_factory import ActionSelection
from factory.reward_factory import RewardFactory


class Env(ABC):
    def __init__(self,env_params:EnvParams) -> None:
        self.env_params = env_params
        self.grid = Grid(size=env_params.GRID_SIZE)
        self.states = [State(row,col) for row in range(self.grid.nrows) for col in range(self.grid.ncols)]
        self.current_state = State(env_params.INITIAL_POS[0],env_params.INITIAL_POS[1])
        self.goal_state = State(env_params.GOAL_POS[0]-1,env_params.GOAL_POS[1]-1)
        self.reward_policy = RewardFactory.get_policy(self.env_params.REWARD_POLICY)

    def reset(self):
        return State(0,0)

    @abstractmethod
    def step(self):
        pass

class GridWorld(Env):

    def __str__(self) -> str:
        return f'GridWorld(size={self.grid})'

    def step(self,state:State,action:ActionSelection):
        next_state = action.step_from(state)
        done = True if next_state == self.goal_state else False
        reward = self.reward_policy.select_reward(done=done)
        # print(f'STEPPING TO {next_state} REWARD = {reward} DONE = {done}')
        return next_state, reward, done
