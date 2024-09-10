class State:
    def __init__(self, row=None, col=None, pos=()) -> None:
        self.row = row if len(pos) == 0 else pos[0]
        self.col = col if len(pos) == 0 else pos[1]

    def __str__(self) -> str:
        return f'State({self.row},{self.col})'
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other) -> bool:
        return self.row == other.row and self.col == other.col
    
    def __hash__(self) -> int:
        return hash((self.row,self.col))