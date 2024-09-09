import numpy as np

from constants import Actions
from entities import QValue

class Agent:
    def __init__(self,states,params):
        self.params = params
        self.estimates = [QValue(state,action,params) for state in states for action in list(Actions)]

    def select_action(self,state):
        """
        selects action based on epsilon-greedy policy
        """
        if np.random.uniform() < self.params.epsilon:
            return np.random.choice(list(Actions))
        else:
            qvalues = [qval for qval in self.estimates if qval.state == state]
            return max(qvalues,key=lambda q: q.Q).action
        
    def update_estimates(self,state,action,reward,next_state,next_action):
        qi = [q for q in self.estimates if q.state == state and q.action == action][0]
        qi_next = [q for q in self.estimates if q.state == next_state and q.action == next_action][0]
        qi.value += self.params.alpha * (reward.value + self.params.gamma * qi_next.value - qi.value)
