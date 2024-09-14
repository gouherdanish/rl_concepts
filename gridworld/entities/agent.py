from typing import List
import numpy as np
from abc import abstractmethod, ABC

from constants import Actions, AgentParams
from entities.state import State
from entities.qvalue import QValue
from factory.action_factory import ActionSelectionFactory

class Agent(ABC):
    def __init__(self,states:List[State],agent_params:AgentParams):
        self.agent_params = agent_params
        self.estimates = {(state,action):QValue(value=0) for state in states for action in list(Actions)}

    def select_action(self,state):
        """
        Selects action based on epsilon-greedy policy
        """
        # Exploration
        if np.random.uniform() < self.agent_params.EPSILON:
            action = np.random.choice(list(Actions))
        # Exploitation
        else:
            q_state = [(a,q) for (s,a), q in self.estimates.items() if s == state]
            action, _ = max(q_state,key=lambda tup: tup[-1])
        return ActionSelectionFactory.get(action)
    
    @abstractmethod
    def update_estimates(self):
        pass