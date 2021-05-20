from mc_api.components.Coordinates import Coordinates
from mc_api.components import BlockState, NBT
from typing import Union

# components

#class Vec3(): ...
class BlockCoordinates(): ...
class Coordinates(): ...


class Block():
    """
    A single '<block>' argument looks like this:

        'stone'
        'minecraft:redstone_wire[power=15,north=up,south=side]'
        'minecraft:jukebox{RecordItem:{...}}'
        'minecraft:furnace[facing=north]{BurnTime:200}'

    The format of '<block>' parameters is 'namespaced_ID[block_states]{data_tags}', in which 
    block states and data tags can be omitted when they are not needed.

        Namespaced ID is required (though if namespace isn't set it defaults to 'minecraft:').
            In the context of "conditions"/testing for blocks, it can also be the namespace ID 
            of block tag with the prefix of '#', such as '#minecraft:planks'.

        Block states are inside '[]', comma-separated and must be properties/values supported 
        by the blocks. They are optional.
            'minecraft:stone[doesntexist=purpleberry]' is a syntax error, because 'stone' 
            doesn't have 'doesntexist'.
            'minecraft:redstone_wire[power=tuesday]' is a syntax error, because 'redstone_wire''s
            'power' is a number between 0 and 15.

        Data tags are inside '{}'. It's optional.

        In the context of "conditions"/testing for blocks, only the states provided are tested.
            If command tests 'redstone_wire[power=15]', it checks only power, but ignores other
            states such as north.

        In the context of setting blocks, any states provided are set, but anything omitted retain 
        their default values, depending on the block.
            If command sets 'redstone_wire[power=15]', it is set 'power' to 15, but 'north' is a
            default value (in this case, set to 'none').
    """
    # dirt
    # minecraft:dirt
    # minecraft:dirt[snowy=true]
    # minecraft:dirt[snowy=true]{onFire:1b, content: {text: "test"}}
    def __init__(self, 
                id: str,
                blockstate: BlockState = BlockState(), 
                nbt: NBT = NBT()):

        # TODO: handle namespace
        
        self.blockstate = blockstate
        self.nbt = nbt

class Zone(): 
    def __init__(self, 
                    pos1: Union[BlockCoordinates, Coordinates, tuple],
                    pos2: Union[BlockCoordinates, Coordinates, tuple]):
        """
        Represents a rectangular zone
        """

class Entity():
    def update_nbt(self): ...
class Player(Entity): ...
class Mob(Entity): ...

class Selector(): ...

# top level functions:

def set_block(coords: Union[BlockCoordinates, tuple], 
                block: Union[Block, str], 
                handler: str = 'replace') -> bool:
    """
    Returns a bool that is set to True
    if no message was sent back by the game

    Available handlers:
        'replace' — The old block drops neither itself nor any contents. Plays no sound.
        'destroy' — The old block drops both itself and its contents (as if destroyed by a player). Plays the appropriate block breaking noise.
        'keep' — Only air blocks are changed (non-air blocks are unchanged).

    Defaults to 'replace'
    """

def set_zone(zone: Union[Zone, tuple(tuple, tuple)],
                block: Union[Block, str],
                handler: str = 'replace') -> bool: 
    """
    Returns a bool that is set to True
    if no message was sent back by the game

    Available handlers:
        'destroy' - Replaces all blocks (including air) in the fill region with the specified block, dropping the existing blocks (including those that are unchanged) and block contents as entities as if they had been mined with an unenchanted diamond shovel or pickaxe. (Blocks that can be mined only with shears, such as vines, do not drop; neither do liquids.)
        'hollow' - Replaces only the blocks on the outer edge of the fill region with the specified block. Inner blocks are changed to air, dropping their contents as entities but not themselves. If the fill region has no inner blocks (because it is smaller than three blocks in at least one dimension), acts like replace.
        'keep' - Replaces only the air blocks in the fill region with the specified block.
        'outline' - Replaces only the blocks on the outer edge of the fill region with the specified block. Inner blocks are not affected. If the fill region has no inner blocks (because it is smaller than three blocks in at least one dimension), acts like replace.
        'replace' - Replaces all blocks (including air) in the fill region with the specified block, without dropping blocks or block contents as entities. Optionally, instead of specifying a data tag for the replacing block, block ID and data values may be specified to limit which blocks are replaced.

    Defaults to 'replace'
    """

def get_block(coords: Union[BlockCoordinates, Coordinates, tuple]) -> Block: 
    """
    Returns a Block component, which contains its representation
    using repr(Block)

    # TODO: Double-check that any coords type can be used here
    """

def get_blocks(zone: Zone) -> list:
    """
    # TODO: its existence is problematic, should it be a method of Zone instead?

    Get the blocks in a rectangular zone

    It returns a tuple containing the blocks
    the zone represents
    """

def get_player(selector: Union[Selector, str]) -> Player: 
    """
    Fill an instance of the component Player with the 
    NBT tags fetched from the Selector component
    or the str passed, evaluated as the name of the player to be fetched.

    # TODO: Use /data get entity wrapped in an execute
    """

def get_players(selector: Selector = '@a') -> list: 
    """
    Fill a list with the players currently
    connected on the server. The list will be populated
    with Player (component) instances.

    A custom selector can be used to filter more accurately.
    By default, selects all the player online.

    # TODO: Use /data get entity wrapped in an execute
    """

def get_entity(selector: Selector) -> Entity:
    """
    Returns an Entity instance populated with the NBT
    tags fetched depending on the selector.

    # TODO: add limit=1 if not provided since this is get_entity
    # TODO: Use /data get entity wrapped in an execute
    """

def get_entities(selector: Selector = None) -> list: ...

def summon_entity(entity): ...
def summom_particles(): ...


def say(): ... 

def whisper(): ...


def title(): ...

def teleport(): ... # tp
def ban(): ... 
def kick(): ... 
def kill(): ...
def op(): ... 

def set_gamemode(): ... 
def whitelist(): ... 
def set_difficulty(): ...

def inventory_give(): ...
def inventory_remove(): ...


def give_effect(): ...
def remove_effect(): ...

def play_sound(): ...

def weather(): ...
def gamerule(): ...

#############
#super functions
###############

# def play_midi(): ... 












#misc