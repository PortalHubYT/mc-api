from mc_api.components import *
from mc_api import NoInterfaceProvided

def setblock(coordinates, block, interface=None):

    if not interface:
        raise NoInterfaceProvided(f'No interface was provided for {__file__}')

    if type(coordinates) is tuple:
        coordinates = Coordinates(*coordinates)
    if type(block) is str:
        block = Block(block)

    cmd = Command('setblock', coordinates, block).to_str()
    response = interface.post(cmd)

    return response
