class BlockState:

    def __init__(self, properties: dict = None):
        
        if type(properties) is dict:
            for key in properties:
                setattr(self, key, properties[key])

        elif properties is not None:
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
        
        buff = ''

        for key in dir(self):
            if key.startswith('__'):
                continue
            elif key == 'flatten':
                continue
        
            value = getattr(self, key)
            value = self.flatten(value)

            buff += f'{key}={value},'

        if len(buff) > 1 and buff[-1] == ',':
            buff = buff[:-1]

        return(f'[{buff}]')

class UnexpectedBlockStatePropertyValueType(Exception):
    pass