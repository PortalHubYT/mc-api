from .server import singleton
from .components import Command

__all__ = [
    "check_output_channel",
    "construct",
    "post",
    "send",
    "default_check",
    "execute_check",
    "unexpected_status",
    "format_arg",
]


def check_output_channel():
    if singleton.check_status():
        return singleton
    else:
        raise NoOutputChannelProvided(f"No output channel was initialized in the code")


def construct(*args):
    return str(Command(*args))


def post(cmd: str):
    return singleton.post(cmd)


def send(*args):
    command = construct(*args)
    response = post(command)
    return response


def default_check(response):
    if response == "":
        return True
    else:
        return response


def execute_check(response):
    if response == "Test passed":
        return True
    elif response == "Test failed":
        return False
    else:
        return response


def unexpected_status(file_name, status):
    raise UnexpectedReturn(
        f'The say command in {file_name.split("/")[-1]} didn\'t properly function and returned: "{status}"'
    )


def format_arg(argument, component):
    if isinstance(argument, component):
        return argument

    if isinstance(argument, str):
        return component(argument)
    elif isinstance(argument, tuple):
        return component(*argument)
    elif isinstance(argument, list):
        return component(*argument)
    else:
        raise InvalidArgumentType(
            f'Invalid argument type, could not parse "{argument}" as a valid component.'
        )


class InvalidArgumentType(Exception):
    pass


class UnexpectedReturn(Exception):
    pass


class NoOutputChannelProvided(Exception):
    pass
