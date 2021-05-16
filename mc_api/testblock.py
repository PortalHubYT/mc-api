from mc_api.components.utils import execute_check
from mc_api.components.BlockCoordinates import BlockCoordinates
from mc_api.components.Subcommand import Subcommand
from mc_api.components import *
from mc_api import NoInterfaceProvided

def testblock(coordinates, block, interface=None):

    if not interface:
        raise NoInterfaceProvided(f'No interface was provided for {__file__}')

    if type(block) is str:
        block = Block(block)

    if type(coordinates) is tuple:
        coordinates = Coordinates(*coordinates)

    # TODO: here
    subcommand = Subcommand('if', 'block')
    block_coordinates = BlockCoordinates(coordinates)

    cmd = Command('execute', subcommand, block_coordinates, block).to_str()
    response = interface.post(cmd)

    status = execute_check(response)

    if status is str:
        raise UnexpectedReturn(f'The command execute didn\'t properly function and returned: "{status}"')

    return status

class UnexpectedReturn(Exception):
    pass