class Command:
    def __init__(self, command, *args):
        self.command = command
        self.args = args
        
    def __repr__(self):
        buff = self.command
        
        if len(self.args) == 0:
            return buff

        for arg in self.args:
            buff += ' '
            buff += repr(arg)
    
        return buff