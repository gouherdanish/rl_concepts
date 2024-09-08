class QValue:
    def __init__(self,Qk=0,k=0) -> None:
        self.Qk = Qk
        self.k = k

    def __str__(self) -> str:
        return f'Q(k={self.k},val={self.Qk})'
    
    def __repr__(self) -> str:
        return str(self)

    def update(self,reward):
        self.k += 1
        self.Qk += (1/self.k)*(reward.value - self.Qk)