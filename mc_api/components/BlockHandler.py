options = ['destroy', 'hollow', 'keep', 'outline', 'replace']

class BlockHandler:
    def __init__(self, type):
        self.type = type

    def to_str(self):
        if self.type not in options:
            raise BlockHandlerWrongType(f'The BlockHandler provided: \'{self.type}\' is not a valid option. Availables: [{" | ".join(options)}]')
        else:
            return(f'{self.type}')

class BlockHandlerWrongType(Exception):
    pass

# DESTROY | HOLLOW | KEEP | OUTLINE | REPLACE

"""DESTROY: Replaces all blocks (including air) in the fill region with the specified block, 
dropping the existing blocks (including those that are unchanged) and block contents 
as entities as if they had been mined with an unenchanted diamond shovel or pickaxe. 
(Blocks that can only be mined with shears, such as vines, will not drop; neither will liquids.)"""
DESTROY = BlockHandler("destroy")

""""HOLLOW: Replaces only blocks on the outer edge of the fill region with the specified block. 
Inner blocks are changed to air, dropping their contents as entities but not themselves. 
If the fill region has no inner blocks (because it is smaller than three blocks 
in at least one dimension), acts like replace."""
HOLLOW = BlockHandler("hollow")

"""KEEP: Replaces only air blocks in the fill region with the specified block."""
KEEP = BlockHandler("keep")

"""OUTLINE: Replaces only blocks on the outer edge of the fill region with the specified block. 
Inner blocks are not affected. If the fill region has no inner blocks 
(because it is smaller than three blocks in at least one dimension), acts like replace."""
OUTLINE = BlockHandler("outline")

"""REPLACE: Replaces all blocks (including air) in the fill region with the specified block,
 without dropping blocks or block contents as entities. Optionally, instead of specifying 
 a data tag for the replacing block, block ID and data values may be specified to limit 
 which blocks are replaced (see replaceTileName and replaceDataValue below)"""
REPLACE = BlockHandler("replace")