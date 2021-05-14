class Coordinates:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z
    
    def to_str(self):
        return (f'{self.x} {self.y} {self.z}')