from abc import abstractmethod, ABC
import numpy as np

from constants import Actions, Params
from entities.state import State

class ActionSelectionFactory:
    registry = {}

    @classmethod
    def register(cls,type):
        def inner(wrapped_cls):
            cls.registry[type] = wrapped_cls
            return wrapped_cls
        return inner
    
    @classmethod
    def get(cls,type,**kwargs):
        return cls.registry[type](**kwargs)

class ActionSelection(ABC):
    def __init__(self) -> None:
        self.step_size = Params.STEP_SIZE

    @abstractmethod
    def step_from(self):
        pass
    
@ActionSelectionFactory.register(Actions.UP)
class UpActionSelection(ActionSelection):

    def __str__(self) -> str:
        return f'UpActionSelection({self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_row = max(state.row-1,0)
        next_col = state.col
        return State(next_row,next_col)

@ActionSelectionFactory.register(Actions.DOWN)
class DownActionSelection(ActionSelection):

    def __str__(self) -> str:
        return f'DownActionSelection({self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_row = min(state.row+1,Params.GRID_SIZE-1)
        next_col = state.col
        return State(next_row,next_col)
    
@ActionSelectionFactory.register(Actions.LEFT)
class LeftActionSelection(ActionSelection):

    def __str__(self) -> str:
        return f'LeftActionSelection({self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_col = max(state.col-1,0)
        next_row = state.row
        return State(next_row,next_col)
    
@ActionSelectionFactory.register(Actions.RIGHT)
class RightActionSelection(ActionSelection):

    def __str__(self) -> str:
        return f'RightActionSelection({self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_col = min(state.col+1,Params.GRID_SIZE-1)
        next_row = state.row
        return State(next_row,next_col)