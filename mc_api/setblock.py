from mc_api.components import *

def setblock(coordinates, block, interface=None):

    if not interface:
        return interface

    if type(coordinates) is tuple:
        coordinates = Coordinates(*coordinates)
    if type(block) is str:
        block = Block(block)

    cmd = Command('setblock', coordinates, block).to_str()
    response = interface.post(cmd)

    return response

    