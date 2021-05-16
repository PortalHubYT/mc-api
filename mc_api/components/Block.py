from mc_api.components.BlockState import BlockState
from .utils import flatten
from .BlockState import BlockState

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
    def __init__(self, id, namespace="minecraft", blockstate=None, metadata=None):
        self.namespace = namespace
        self.id = id

        self.blockstate = blockstate
        self.metadata = metadata
    
    def to_str(self):
        buff = f'{self.namespace}:{self.id}'
        if self.blockstate:
            buff += '['
            if isinstance(self.blockstate, list):
                for blockstate in self.blockstate[:-1]:
                    buff += flatten(blockstate)
                    buff += ','
                buff += flatten(self.blockstate[-1])
            elif isinstance(self.blockstate, BlockState):
                buff += flatten(self.blockstate)
            buff += ']'
        
        return buff