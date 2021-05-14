class BlockState:
    def __init__(self, type):
        self.type = type

    def to_str(self):
        return(f'{self.type}')