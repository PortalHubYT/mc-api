from mc_api.components import Block, Subcommand, BlockCoordinates
from .base_functions import *

def _test_block(block_coordinates: BlockCoordinates, block: Block):

    subcommand = Subcommand('if', 'block')

    response = send('execute', subcommand, block_coordinates, block)

    status = execute_check(response)

    if status is str:
        unexpected_status(__file__, status)

    return status

def test_block(block_coordinates: BlockCoordinates or tuple, 
                block: Block or str) -> bool: 
                
    check_output_channel()

    block_coordinates = format_arg(block_coordinates, BlockCoordinates)
    block = format_arg(block, Block)
    
    return _test_block(block_coordinates, block)
    