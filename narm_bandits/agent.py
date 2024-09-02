from abc import abstractmethod
import numpy as np

from qvalue import QValue

class Agent:
    def __init__(self,n_actions,epsilon=0) -> None:
        self.n_actions = n_actions
        self.epsilon = epsilon
        self.qarr = [QValue() for _ in range(n_actions)]

    def __str__(self) -> str:
        return f'Agent(epsilon={self.epsilon},Q={self.qarr})'

    def select_action(self):
        if np.random.random() < self.epsilon:
            np.random.choice(self.n_actions)
        else:
            self.qvalues = np.array([q.Qk for q in self.qarr])
            return np.argmax(self.qvalues)

    def update_estimates(self,a,r):
        self.qarr[a].update(r)
