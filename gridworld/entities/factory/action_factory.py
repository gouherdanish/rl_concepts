from abc import abstractmethod, ABC
import numpy as np

from constants import Actions

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
    @abstractmethod
    def _select_action(self):
        pass

    def select_Action(self):
        Action = self._select_action()
        return Action(value=Action)
    
@ActionSelectionFactory.register(Actions.UP.value)
class UpActionSelection(ActionSelection):
    def __str__(self) -> str:
        return f'UpActionSelection({self.action_dist})'
    
    def __repr__(self) -> str:
        return str(self)

    def step(self,state):
        return self.action_dist[0]

@ActionSelectionFactory.register(Actions.UP.value)
class DownActionSelection(ActionSelection):
    def __str__(self) -> str:
        return f'DownActionSelection({self.action_dist})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def step(self):
        return np.random.choice(self.action_dist)
    
@ActionSelectionFactory.register('normal')
class NormalActionSelection(ActionSelection):
    def __init__(self, mean=0, std=1) -> None:
        self.mean = mean
        self.std = std

    def __str__(self) -> str:
        return f'NormalActionSelection({self.mean},{self.std})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def _select_action(self):
        return np.random.normal(loc=self.mean,scale=self.std)