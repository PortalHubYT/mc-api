class Command:
    def __init__(self, command: str, *args):
        self.command = command
        self.args = args
    
    def to_str():
        pass
    
    def __repr__(self):
        buff = self.command
        
        if len(self.args) == 0:
            return buff

        for arg in self.args:
            buff += ' '
            buff += repr(arg)
    
        return buff