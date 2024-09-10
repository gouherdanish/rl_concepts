class Grid:
    def __init__(self,size) -> None:
        self.size = size
        self.nrows = size[0]
        self.ncols = size[1]
    
    def __str__(self) -> str:
        return f'Grid({self.size})'