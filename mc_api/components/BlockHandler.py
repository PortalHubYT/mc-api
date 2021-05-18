from mc_api.components import Block

options = ['destroy', 'hollow', 'keep', 'outline', 'replace']

class BlockHandler:
    def __init__(self, mode: str, option: Block = None):
        self.mode = mode
        self.option = option

    def __repr__(self):
        if self.mode == 'replace':
            if type(self.option) is not Block:
                raise BlockHandlerWrongType(f'The BlockHandler option provided: \'{self.option}\' is not a valid option for the block handler "replace".')
                
        if self.mode not in options:
            raise BlockHandlerWrongType(f'The BlockHandler provided: \'{self.mode}\' is not a valid option. Availables: [{" | ".join(options)}]')
        elif self.option:
            return(f'{self.mode} {repr(self.option)}')
        else:
            return(f'{self.mode}')

class BlockHandlerWrongType(Exception):
    pass

class BlockHandlerWrongOption(Exception):
    pass

"""DESTROY: Replaces all blocks (including air) in the fill region with the specified block, 
dropping the existing blocks (including those that are unchanged) and block contents 
as entities as if they had been mined with an unenchanted diamond shovel or pickaxe. 
(Blocks that can only be mined with shears, such as vines, will not drop; neither will liquids.)

HOLLOW: Replaces only blocks on the outer edge of the fill region with the specified block. 
Inner blocks are changed to air, dropping their contents as entities but not themselves. 
If the fill region has no inner blocks (because it is smaller than three blocks 
in at least one dimension), acts like replace.

KEEP: Replaces only air blocks in the fill region with the specified block.

OUTLINE: Replaces only blocks on the outer edge of the fill region with the specified block. 
Inner blocks are not affected. If the fill region has no inner blocks 
(because it is smaller than three blocks in at least one dimension), acts like replace.

REPLACE: Replaces all blocks (including air) in the fill region with the specified block,
without dropping blocks or block contents as entities. Optionally, instead of specifying 
a data tag for the replacing block, block ID and data values may be specified to limit 
which blocks are replaced (see replaceTileName and replaceDataValue below)"""