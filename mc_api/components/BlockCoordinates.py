import math

class BlockCoordinates:
    """
    The position of a block is actually the coordinates of the point at the lower northwest corner
    of the block, that is, the integer coordinates obtained by rounding down the coordinates 
    inside the block.

    In Minecraft, decimal coordinates usually needs to be converted into integer coordinates by rounding
    down, which is called the block position of the coordinate. 
    """
    def __init__(self, x: int, y: int, z: int):
        self.x = math.floor(x)
        self.y = math.floor(y)
        self.z = math.floor(z)
    
    def __repr__(self):
        return (f'{self.x} {self.y} {self.z}')