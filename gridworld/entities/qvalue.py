class QValue:
    def __init__(self,state,action,params) -> None:
        self.state = state
        self.action = action
        self.params = params
        self.value = 0

    def update(self,reward):
        self.Q += self.params.alpha * (reward.value + self.params.gamma *  - self.Q)