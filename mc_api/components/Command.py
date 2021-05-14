class Command:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def to_str(self):
        #TO-DO: Test this, that args correctly unpack
        return(f'{self.name} {" ".join([arg.to_str() for arg in self.args])}')