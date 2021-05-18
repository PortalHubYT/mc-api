from mc_api.components import Block, BlockCoordinates, Zone
from .base_functions import *

def _set_zone(zone: Zone, block: Block) -> str:
    response = send('fill', zone, block)

    return response

def set_zone(pos1: BlockCoordinates or tuple,
                pos2: BlockCoordinates or tuple,
                block: Block or str) -> str:
    
    check_output_channel()

    pos1 = format_arg(pos1, BlockCoordinates)
    pos2 = format_arg(pos2, BlockCoordinates)
    block = format_arg(block, Block)

    zone = Zone(pos1, pos2)

    return _set_zone(zone, block)
    
    