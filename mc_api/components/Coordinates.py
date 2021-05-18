class Coordinates:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return (f'{self.x} {self.y} {self.z}')