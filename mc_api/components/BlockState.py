class BlockState:

    def __init__(self, properties: dict = None):
        
        self.buff = ''

        if type(properties) is dict:

            for key in properties:
            
                properties[key] = self.flatten(properties[key])

                self.buff += f'{key}={properties[key]},'

        else:
            raise ValueError("BlockState arg must be a dictionnary")

    def flatten(self, arg):
        if type(arg) is int:
            return(str(arg))

        elif type(arg) is bool:
            if arg is True:
                return('true')
            else:
                return('false')
        
        elif type(arg) is str:
            return(arg)
        
        else:
            raise UnexpectedBlockStatePropertyValueType(f'The type of: [{arg}] is [{type(arg)}] and is not valid for blockstate. The value must either be an int, a boolean or a string')

    def __repr__(self):
        
        for key in dir(self):
            if key.startswith('__'):
                continue
            elif key in ['buff', 'flatten']:
                continue
        
            value = getattr(self, key)
            value = self.flatten(value)

            self.buff += f'{key}={value},'

        if len(self.buff) > 1 and self.buff[-1] == ',':
            self.buff = self.buff[:-1]

        return(f'[{self.buff}]')

class UnexpectedBlockStatePropertyValueType(Exception):
    pass