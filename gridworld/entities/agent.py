import numpy as np

from constants import Actions, Params

class Agent:
    def __init__(
            self,
            states,
            epsilon,
            alpha,
            gamma) -> None:
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.estimates = {(state,action):0 for state in states for action in Actions}

    def select_action(self,state):
        """
        selects action based on epsilon-greedy policy
        """
        if np.random.uniform() < self.epsilon:
            return np.random.choice(list(Actions))
        else:
            return Actions