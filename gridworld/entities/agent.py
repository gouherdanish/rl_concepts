import numpy as np

from constants import Actions
from entities.qvalue import QValue
from factory.action_factory import ActionSelectionFactory

class Agent:
    def __init__(self,states,agent_params):
        self.agent_params = agent_params
        self.estimates = {(state,action):QValue() for state in states for action in list(Actions)}

    def select_action(self,state):
        """
        selects action based on epsilon-greedy policy
        """
        if np.random.uniform() < self.agent_params.epsilon:
            action = np.random.choice(list(Actions))
        else:
            q_state = [(a,q) for (s,a), q in self.estimates.items() if s == state]
            action, _ = max(q_state,key=lambda tup: tup[-1])
        return ActionSelectionFactory.get(action)
        
    def update_estimates(self,state,action,reward,next_state,next_action):
        qi = self.estimates[(state,action)]
        qi_next = self.estimates[(next_state,next_action)]
        # qi = [q for q in self.estimates if q.state == state and q.action == action][0]
        # qi_next = [q for q in self.estimates if q.state == next_state and q.action == next_action][0]
        qi.value += self.agent_params.alpha * (reward.value + self.agent_params.gamma * qi_next.value - qi.value)
