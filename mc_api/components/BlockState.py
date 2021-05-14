class BlockState:
    def __init__(self):
        self.property = None
        self.value = None

    def to_str(self):
        if self.property and self.value:
            return(f'[{self.property}={self.value}]')
        else:
            return(f'')