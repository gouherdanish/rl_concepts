from abc import abstractmethod, ABC
import numpy as np

from constants import Actions, EnvParams
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
        self.step_size = EnvParams.STEP_SIZE

    @abstractmethod
    def step_from(self):
        pass
    
@ActionSelectionFactory.register(Actions.UP)
class UpActionSelection(ActionSelection):
    def __init__(self) -> None:
        super().__init__()
        self.action = Actions.UP

    def __str__(self) -> str:
        return f'ActionSelection(action={self.action},step_size={self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_row = max(state.row-1,0)
        next_col = state.col
        return State(next_row,next_col)

@ActionSelectionFactory.register(Actions.DOWN)
class DownActionSelection(ActionSelection):
    def __init__(self) -> None:
        super().__init__()
        self.action = Actions.DOWN

    def __str__(self) -> str:
        return f'ActionSelection(action={self.action},step_size={self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_row = min(state.row+1,EnvParams.GRID_SIZE[0]-1)
        next_col = state.col
        return State(next_row,next_col)
    
@ActionSelectionFactory.register(Actions.LEFT)
class LeftActionSelection(ActionSelection):
    def __init__(self) -> None:
        super().__init__()
        self.action = Actions.LEFT

    def __str__(self) -> str:
        return f'ActionSelection(action={self.action},step_size={self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_col = max(state.col-1,0)
        next_row = state.row
        return State(next_row,next_col)
    
@ActionSelectionFactory.register(Actions.RIGHT)
class RightActionSelection(ActionSelection):
    def __init__(self) -> None:
        super().__init__()
        self.action = Actions.RIGHT

    def __str__(self) -> str:
        return f'ActionSelection(action={self.action},step_size={self.step_size})'
    
    def __repr__(self) -> str:
        return str(self)

    def step_from(self,state):
        next_col = min(state.col+1,EnvParams.GRID_SIZE[1]-1)
        next_row = state.row
        return State(next_row,next_col)