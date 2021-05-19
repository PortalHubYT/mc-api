from mc_api.components.BlockState import BlockState
from mc_api.components import Block, BlockCoordinates, BlockHandler
from mc_api.base_functions import *

def _set_block(block_coordinates: BlockCoordinates, 
                block: Block,
                block_handler: BlockHandler = None):

    if block_handler:
        response = send('setblock', block_coordinates, block, block_handler)
    else:
        response = send('setblock', block_coordinates, block)
        
    status = execute_check(response)

    if status is str:
        unexpected_status(__file__, status)

    return status

def set_block(block_coordinates: BlockCoordinates or tuple, 
                block: Block or str,
                block_handler: BlockHandler or str = None,
                block_handler_option: Block or str = None) -> bool:
    
    check_output_channel()

    block_coordinates = format_arg(block_coordinates, BlockCoordinates)
    block = format_arg(block, Block)

    if block_handler:
        block_handler = format_arg(block_handler, BlockHandler)

        if block_handler_option:
            block_handler_option = format_arg(block_handler_option, Block)
            block_handler.option = block_handler_option
    
    return _set_block(block_coordinates, block, block_handler)

meta_definition = {
    "setblock": {
      "type": "literal",
      "children": {
        "pos": {
          "type": "argument",
          "parser": BlockCoordinates,
          "children": {
            "block": {
              "type": "argument",
              "parser": BlockState,
              "children": {
                "destroy": {
                  "type": "literal",
                  "executable": True
                },
                "keep": {
                  "type": "literal",
                  "executable": True
                },
                "replace": {
                  "type": "literal",
                  "executable": True
                }
              },
              "executable": True
            }
          }
        }
      }
    }
}