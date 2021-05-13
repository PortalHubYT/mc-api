from container_connecter import ServerInstance

mc = ServerInstance()

class Coordinates:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z
    
    def to_str(self):
        return (f'{self.x} {self.y} {self.z}')

class Block:
    def __init__(self, id, namespace="minecraft"):
        self.namespace = namespace
        self.id = id

    def to_str(self):
        return (f'{self.namespace}:{self.id}')

class Metadata:
    def __init__(self, value):
        self.value = value

    def to_str(self):
        return (f'{self.value}')

class BlockHandler:
    def __init__(self, type):
        self.type = type
    
    def to_str(self):
        return(f'{self.type}')

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

class Command:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def to_str(self):
        #TO-DO: Test this, that args correctly unpack
        return(f'{self.name} {" ".join([arg.to_str() for arg in self.args])}')

def setblock(coords, block, block_handler=REPLACE): 
    command = Command("setblock", [coords, block, block_handler])
    mc.post(command.to_str())
