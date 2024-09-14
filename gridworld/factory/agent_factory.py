
from entities.agent import Agent
from factory.action_factory import ActionSelectionFactory

class AgentFactory:
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

@AgentFactory.register('sarsa')
class SarsaAgent(Agent):
    def __str__(self) -> str:
        return f'SarsaAgent(estimates={self.estimates})'
        
    def update_estimates(self,state,action,reward,next_state,next_action):
        """
        Implements SARSA Update Policy
        """
        qi = self.estimates[(state,action)]
        qi_next = self.estimates[(next_state,next_action)]
        print(qi_next)
        qi.value += self.agent_params.ALPHA * (reward + self.agent_params.GAMMA * qi_next.value - qi.value)

@AgentFactory.register('qlearning')
class QLearningAgent(Agent):
    def __str__(self) -> str:
        return f'QLearningAgent(estimates={self.estimates})'
        
    def update_estimates(self,state,action,reward,next_state):
        """
        Implements Q-Learning Update Policy
        """
        qi = self.estimates[(state,action)]
        qi_next = [q for (s,_), q in self.estimates.items() if s == next_state]
        print(f'{next_state}:{qi_next}')
        qi.value += self.agent_params.ALPHA * (reward + self.agent_params.GAMMA * max(qi_next).value - qi.value)
