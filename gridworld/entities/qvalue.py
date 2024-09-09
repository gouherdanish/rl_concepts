class QValue:
    def __init__(self,state,action,params) -> None:
        self.state = state
        self.action = action
        self.params = params
        self.value = 0