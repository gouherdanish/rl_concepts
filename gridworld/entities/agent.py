from typing import List
import numpy as np

from constants import Actions, AgentParams
from entities.state import State
from entities.qvalue import QValue
from factory.action_factory import ActionSelectionFactory

class Agent:
    def __init__(
            self,
            states:List[State],
            agent_params:AgentParams):
        self.agent_params = agent_params
        self.estimates = {(state,action):QValue(value=0) for state in states for action in list(Actions)}

    def __str__(self) -> str:
        return f'Agent(estimates={self.estimates})'

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
        
    def update_estimates(self,state,action,reward,next_state,next_action):
        """
        Implements SARSA Update Policy
        """
        qi = self.estimates[(state,action)]
        qi_next = self.estimates[(next_state,next_action)]
        qi.value += self.agent_params.ALPHA * (reward + self.agent_params.GAMMA * qi_next.value - qi.value)
