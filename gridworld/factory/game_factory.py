from abc import abstractmethod, ABC
import numpy as np

from entities.agent import Agent
from entities.env import GridWorld
from entities.game import Game

class GameFactory:
    registry = {}

    @classmethod
    def register(cls,method):
        def inner(wrapped_cls):
            cls.registry[method] = wrapped_cls
            return wrapped_cls
        return inner
    
    @classmethod
    def get(cls,method,**kwargs):
        return cls.registry[method](**kwargs)
    
@GameFactory.register('sarsa')
class SarsaRL(Game):
    def __str__(self) -> str:
        return f'SarsaRL(Agent={self.agent},Env={self.env})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def run(self,episodes):
        for episode in range(episodes):
            print(f"<<<<< EPISODE {episode+1} START >>>>>")
            state = self.env.reset()
            action = self.agent.select_action(state)
            print(state,action)
            done = False
            while not done :
                next_state, reward, done = self.env.step(state,action)
                next_action = self.agent.select_action(next_state)
                sarsa = (state,action.action,reward,next_state,next_action.action)
                self.agent.update_estimates(*sarsa)
                state = next_state
                action = next_action
                print([(s,a,q) for (s,a), q in self.agent.estimates.items() if q.value != 0])
            print(f"<<<<< EPISODE {episode+1} END >>>>>")

@GameFactory.register('qlearning')
class QLearningRL(Game):
    def __str__(self) -> str:
        return f'QLearningRL(Agent={self.agent},Env={self.env})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def run(self,episodes):
        for episode in range(episodes):
            print(f"<<<<< EPISODE {episode+1} START >>>>>")
            state = self.env.reset()
            done = False
            while not done :
                action = self.agent.select_action(state)
                next_state, reward, done = self.env.step(state,action)
                params = (state,action.action,reward,next_state)
                self.agent.update_estimates(*params)
                state = next_state
                print([(s,a,q) for (s,a), q in self.agent.estimates.items() if q.value != 0])
            print(f"<<<<< EPISODE {episode+1} END >>>>>")
