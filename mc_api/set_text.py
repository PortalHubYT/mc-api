from mc_api.components import Block, BlockCoordinates
from mc_api.base_functions import *
from mc_api.set_block import _set_block

def _set_text(message: str, 
                coords: BlockCoordinates or tuple, 
                block: Block or str,
                option: str):

    for letter in message:
        for digit in letters_dict[letter][option]:
            _set_block(coords, block)

def set_text(message: str, 
                coords: BlockCoordinates or tuple, 
                block: Block or str,
                option: str = 'smallcaps'):
    
    """
    The given coord should represent the block that is
    lower northwest corner of the structure

    options are:
    - smallcaps
    - lowercase
    - uppercase
    """

    check_output_channel()

    coords = format_arg(coords, BlockCoordinates)
    block = format_arg(block, Block)

    return _set_text(message, coords, block, option)

meta_definition = "custom"

# Legend: 
# 0 = void
# 1 = block
# 2 = up slab
# 3 = low slab
# for the 4 stairs below, they are represented by where their empty quarter of block is
# 4 = upper left
# 5 = upper right
# 6 = bottom left
# 7 = bottom right
# each letter is represented by a string of 15 digits,
# separated by a dash for each new column,
# representing a letter in a 3*5 block format

letters_dict = {
    "a": {
        "smallcaps": "000-425-131-101-000",
        "uppercase": "425-101-121-101-000",
        "lowercase": "000-425-221-636-000"
    },
    "b": {
        "smallcaps": "000-124-124-137-000",
        "uppercase": "125-135-101-137-000",
        "lowercase": "100-125-101-737-000"
    },
    "c": {
        "smallcaps": "000-425-100-537-000",
        "uppercase": "425-100-100-637-000",
        "lowercase": "000-435-100-637-000"
    },
    "d": {
        "smallcaps": "000-125-101-137-000",
        "uppercase": "125-101-101-137-000",
        "lowercase": "001-421-101-636-000"
    },
    "e": {
        "smallcaps": "000-122-120-133-000",
        "uppercase": "122-130-100-133-000",
        "lowercase": "000-425-122-637-000"
    },
    "f": {
        "smallcaps": "000-122-120-100-000",
        "uppercase": "122-130-100-100-000",
        "lowercase": "425-130-100-100-000"
    },
    "g": {
        "smallcaps": "000-425-103-634-000",
        "uppercase": "425-100-106-637-000",
        "lowercase": "000-424-101-021-637"
    },
    "h": {
        "smallcaps": "000-101-121-101-000",
        "uppercase": "101-131-101-101-000",
        "lowercase": "100-125-101-101-000"
    },
    "i": {
        "smallcaps": "000-212-010-313-000",
        "uppercase": "212-010-010-313-000",
        "lowercase": "020-210-010-313-000"
    },
    "j": {
        "smallcaps": "000-001-001-637-000",
        "uppercase": "001-001-001-637-000",
        "lowercase": "002-021-001-001-637"
    },
    "k": {
        "smallcaps": "000-107-163-101-000",
        "uppercase": "107-140-105-101-000",
        "lowercase": "100-103-160-105-000"
    },
    "l": {
        "smallcaps": "000-100-100-133-000",
        "uppercase": "100-100-100-133-000",
        "lowercase": "100-100-100-637-000"
    },
    "m": {
        "smallcaps": "000-504-111-101-000",
        "uppercase": "504-111-101-101-000",
        "lowercase": "000-555-111-101-000"
    },
    "n": {
        "smallcaps": "000-501-161-106-000",
        "uppercase": "501-151-161-106-000",
        "lowercase": "000-525-101-101-000"
    },
    "o": {
        "smallcaps": "000-435-101-637-000",
        "uppercase": "425-101-101-637-000",
        "lowercase": "000-425-101-637-000"
    },
    "p": {
        "smallcaps": "000-126-137-100-000",
        "uppercase": "125-101-120-100-000",
        "lowercase": "000-525-101-137-100"
    },
    "q": {
        "smallcaps": "000-425-101-645-000",
        "uppercase": "425-101-101-645-000",
        "lowercase": "000-424-101-631-001"
    },
    "r": {
        "smallcaps": "000-125-137-101-000",
        "uppercase": "125-107-121-101-000",
        "lowercase": "000-575-100-100-000"
    },
    "s": {
        "smallcaps": "000-425-263-637-000",
        "uppercase": "425-630-001-637-000",
        "lowercase": "000-425-263-637-000"
    },
    "t": {
        "smallcaps": "000-212-010-010-000",
        "uppercase": "212-010-010-010-000",
        "lowercase": "040-212-010-063-000"
    },
    "u": {
        "smallcaps": "000-101-101-637-000",
        "uppercase": "101-101-101-637-000",
        "lowercase": "000-101-101-636-000"
    },
    "v": {
        "smallcaps": "000-101-607-010-000",
        "uppercase": "101-101-607-010-000",
        "lowercase": "000-101-607-010-000"
    },
    "w": {
        "smallcaps": "000-101-131-706-000",
        "uppercase": "101-101-131-706-000",
        "lowercase": "000-101-131-627-000"
    },
    "x": {
        "smallcaps": "000-637-010-425-000",
        "uppercase": "607-010-010-405-000",
        "lowercase": "000-637-010-425-000"
    },
    "y": {
        "smallcaps": "000-637-010-010-000",
        "uppercase": "101-637-010-010-000",
        "lowercase": "000-101-101-021-637"
    },
    "z": {
        "smallcaps": "000-267-010-453-000",
        "uppercase": "221-047-470-133-000",
        "lowercase": "000-267-010-453-000"
    }
}