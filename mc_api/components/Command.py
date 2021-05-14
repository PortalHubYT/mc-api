class Command:
    def __init__(self, name, args=None):
        self.name = name
        self.args = args

    def to_str(self):
        if self.args:
            return(f'{self.name} {" ".join([arg.to_str() for arg in self.args])}')
        else:
            return(f'{self.name}')
