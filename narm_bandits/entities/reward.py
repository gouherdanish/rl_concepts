class Reward:
    def __init__(self,value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'Reward({self.value})'
    
    def __repr__(self) -> str:
        return str(self)