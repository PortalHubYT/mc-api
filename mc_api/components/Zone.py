from typing import Union

from .BlockCoordinates import BlockCoordinates

class Zone:
    """
    Custom component that is a set of two Coordinates(), representing
    a rectangular area
    """
    def __init__(self, pos1: Union[BlockCoordinates, tuple], 
                        pos2: Union[BlockCoordinates, tuple]):

        if type(pos1) is tuple:
            self.pos1 = BlockCoordinates(*pos1)
        else:
            self.pos1 = pos1

        if type(pos2) is tuple:
            self.pos2 = BlockCoordinates(*pos2)
        else:
            self.pos2 = pos2

    def __repr__(self):
        if type(self.pos1) is not BlockCoordinates or type(self.pos2) is not BlockCoordinates:
            raise ZoneWrongCoordsType('a Zone requires to be provided a set of two BlockCoordinates instances as pos1 and pos2')

        return (f'{repr(self.pos1)} {repr(self.pos2)}')

class ZoneWrongCoordsType(Exception):
    pass
    