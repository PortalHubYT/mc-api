class BlockState:
    def __init__(self, property=None, value=None):
        self.property = property
        self.value = value

    def to_str(self):
        if self.property and self.value:
            return(f'{self.property}={self.value}')
        else:
            return(f'')