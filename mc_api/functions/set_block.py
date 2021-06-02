from typing import Union

from mc_api.components.Block import Block
from mc_api.components.BlockState import BlockState
from mc_api.components.BlockCoordinates import BlockCoordinates
from mc_api.components.BlockHandler import BlockHandler

from mc_api.functions.base_functions import *


def _set_block(coords: BlockCoordinates, block: Block, handler: BlockHandler) -> str:
    return f"setblock {coords} {block} {handler}"


def set_block(
    coords: Union[BlockCoordinates, tuple],
    block: Union[Block, str],
    handler: Union[BlockHandler, str] = "replace",
) -> Union[bool, str]:
    """
    Returns a bool that is set to True
    if no message was sent back by the game or the
    message itself if there was an issue

    Available handlers:
        'replace' — The old block drops neither itself nor any contents. Plays no sound.
        'destroy' — The old block drops both itself and its contents (as if destroyed by a player). Plays the appropriate block breaking noise.
        'keep' — Only air blocks are changed (non-air blocks are unchanged).

    Defaults to 'replace'
    """

    check_output_channel()

    coords = format_arg(coords, BlockCoordinates)
    block = format_arg(block, Block)
    handler = format_arg(handler, BlockHandler)

    cmd = _set_block(coords, block, handler)

    status = post(cmd)

    return True if status.startswith("Changed the block") else status


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
                            "destroy": {"type": "literal", "executable": True},
                            "keep": {"type": "literal", "executable": True},
                            "replace": {"type": "literal", "executable": True},
                        },
                        "executable": True,
                    }
                },
            }
        },
    }
}
