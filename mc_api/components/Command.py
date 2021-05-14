from .utils import flatten

class Command:
    def __init__(self, command, *args):
        self.command = command
        self.args = args
        
    def to_str(self):
        buff = self.command + ' '
        for a in self.args[:-1]:
            buff += flatten(a)
            buff += ' '
        buff += flatten(self.args[-1])
        return buff