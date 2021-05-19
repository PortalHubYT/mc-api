from mc_api.components import Block, BlockCoordinates, Zone, BlockHandler
from .base_functions import *

def _set_zone(zone: Zone, 
                block: Block, 
                block_handler: BlockHandler) -> str:

    if block_handler:
        response = send('fill', zone, block, block_handler)
    else: 
        response = send('fill', zone, block)

    return response

def set_zone(pos1: BlockCoordinates or tuple,
                pos2: BlockCoordinates or tuple,
                block: Block or str,
                block_handler: BlockHandler or str = None,
                block_handler_option: Block or str = None) -> str:
    
    check_output_channel()

    pos1 = format_arg(pos1, BlockCoordinates)
    pos2 = format_arg(pos2, BlockCoordinates)
    block = format_arg(block, Block)

    if block_handler:
        block_handler =  (block_handler, BlockHandler)

        if block_handler_option:
            block_handler_option = format_arg(block_handler_option, Block)
            block_handler.option = block_handler_option

    zone = Zone(pos1, pos2)

    return _set_zone(zone, block, block_handler, block_handler_option)
    
meta_definition = "custom"