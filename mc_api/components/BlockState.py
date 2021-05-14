class BlockState:
    def __init__(self):
        self.key = key
        self.value = value

    def to_str(self):
        return(f'[{self.type}={self.value}]')