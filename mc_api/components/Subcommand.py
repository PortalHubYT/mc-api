options = ['align', 'anchored', 'as', 'at', 'facing', 'in', 
            'positioned', 'rotated', 'store', 'if', 'unless']

class Subcommand:
    def __init__(self, type):
        self.type = type

    def to_str(self):
        if self.type not in options:
            raise SubcommandWrongType(f'The BlockHandler provided: \'{self.type}\' is not a valid option. Availables: [{" | ".join(options)}]')
        else:
            return(f'{self.type}')

class SubcommandWrongType(Exception):
    pass