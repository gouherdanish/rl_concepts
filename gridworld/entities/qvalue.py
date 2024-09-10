class QValue:
    def __init__(self,value=0) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'Q({self.value})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __lt__(self,other):
        return self.value < other.value