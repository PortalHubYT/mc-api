from mc_api.components import BlockCoordinates
from .base_functions import *

def _get_block(block_coordinates: BlockCoordinates) -> str:
    void_coordinates = BlockCoordinates(block_coordinates.x, -64, block_coordinates.y)

    response = send(f'loot spawn {repr(void_coordinates)} mine {repr(block_coordinates)}')
    response = response.split('/')[-1]

    return response

def get_block(block_coordinates: BlockCoordinates or tuple) -> str:
    """
    with “/loot ... mine <x y z> diamond_pickaxe{Enchantments:[{id:silk_touch,lvl:1}]}”, 
    grab the id from the dropped loot and you’re good to go. There are some blocks this 
    doesn’t apply for, barriers, bedrock, structure/command blocks, end portal frame, 
    but you’ll be able to hard code those your
    """
    # TODO: Add a better implementation of fetching block id
    # TODO: Update this function to implement returning block_state and metadata from the block fetched
    # TODO: (Not Important) Add arguments depth to the loot function

    check_output_channel()

    block_coordinates = format_arg(block_coordinates, BlockCoordinates)

    return _get_block(block_coordinates)

meta_definition = "custom"