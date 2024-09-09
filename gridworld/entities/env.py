from abc import ABC, abstractmethod

from constants import EnvParams
from entities.grid import Grid
from entities.state import State
from factory.action_factory import ActionSelectionFactory
from factory.reward_factory import RewardFactory


class Env(ABC):
    def __init__(self,env_params:EnvParams) -> None:
        self.env_params = env_params
        self.grid = Grid(size=env_params.GRID_SIZE)
        self.states = [State(row,col) for row in self.grid.rows for col in self.grid.cols]
        self.current_state = State(env_params.INITIAL_POS[0],env_params.INITIAL_POS[1])
        self.goal_state = State(env_params.GOAL_POS[0],env_params.GOAL_POS[1])
        self.reward_policy = RewardFactory.get_policy(self.env_params.REWARD_POLICY,states=self.states)

    def reset(self):
        return State(0,0)

    @abstractmethod
    def step(self):
        pass

class GridWorld(Env):

    def step(self,state,action):
        action_selector = ActionSelectionFactory.get(action)
        next_state = action_selector.step_from(state)

        reward, done = self.reward_policy.select_reward(next_state)
        done = True if next_state == self.goal_state else False
        return next_state, reward, done
