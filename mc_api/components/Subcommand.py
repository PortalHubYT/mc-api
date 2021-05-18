options = ['align', 'anchored', 'as', 'at', 'facing', 'in', 
            'positioned', 'rotated', 'store', 'if', 'unless']

conditions = ['block', 'blocks', 'data', 'entity',
                'predicate', 'score']

class Subcommand:
    def __init__(self, type, condition=None):
        self.type = type
        self.condition = condition

        if self.type == 'if' or self.type == 'unless':
            if not self.condition:
                raise ConditionRequired(f'The command: "execute (if|unless)" requires one of the following condition: [{" | ".join(conditions)}]')

            if self.condition not in conditions:
                raise ConditionInvalid(f'The condition provided: \'{self.condition}\' is not valid option. Availables: [{" | ".join(conditions)}]')

    def __repr__(self):
        if self.type not in options:
            raise SubcommandWrongType(f'The subcommand provided: \'{self.type}\' is not a valid option. Availables: [{" | ".join(options)}]')
        elif self.condition:
            return(f'{self.type} {self.condition}')
        else:
            return(f'{self.type}')

class SubcommandWrongType(Exception):
    pass

class ConditionRequired(Exception):
    pass

class ConditionInvalid(Exception):
    pass