from .utils import flatten

class Command:
    def __init__(self, command, *args):
        self.command = command
        self.args = args
        
    def to_str(self):
        buff = self.command
        
        if len(self.args) == 0:
            return buff

        for a in self.args:
            buff += ' '
            buff += flatten(a)
    
        return buff