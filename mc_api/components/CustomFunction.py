from mc_api.components.Command import Command

class CustomFunction:

    def construct(self, *args):
        return Command(*args).to_str()

    def post(self, cmd: str):
        return self.interface.post(cmd)

    def send(self, *args):
        self.command = self.construct(*args)
        self.response = self.post(self.command)
        return self.response

    def check_interface(self, interface, file_name: str):
        if interface is None:
            raise NoInterfaceProvided(f'No interface was provided for {file_name}')
        else:
            return interface
    
    def format_arg(self, argument, component):
        if type(argument) is component:
            return argument
            
        if type(argument) is str:
            return component(argument)
        elif type(argument) is tuple:
            return component(*argument)
        elif type(argument) is list:
            return component(*argument)
        else:
            raise InvalidArgumentType(f'Invalid argument type for {__file__}, could not parse "{argument}" as a valid component.')

    def default_check(self, response):
        if response == '':
            return True
        else:
            return response

    def execute_check(self, response):
        if response == 'Test passed':
            return True
        elif response == 'Test failed':
            return False
        else:
            return response

class InvalidArgumentType(Exception):
    pass

class NoInterfaceProvided(Exception):
    pass