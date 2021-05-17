from mc_api.server.interface import interface
from mc_api.components.Command import Command
from mc_api.components.utils import trim_file_name

class CustomFunction:

    def construct(self, *args):
        return Command(*args).to_str()

    def post(self, cmd: str):
        return interface.post(cmd)

    def send(self, *args):
        self.command = self.construct(*args)
        self.response = self.post(self.command)
        return self.response

    def check_interface(self):
        if interface.check_status():
            return interface
        else:
            raise NoInterfaceProvided(f'No interface was initialized in the code')
    
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

    def unexpected_status(self, file_name, status, command):
        raise UnexpectedReturn(f'The say command in {trim_file_name(file_name)} didn\'t properly function and returned: "{status}" with the command "{command}"')


class InvalidArgumentType(Exception):
    pass

class NoInterfaceProvided(Exception):
    pass

class UnexpectedReturn(Exception):
    pass