from collections import namedtuple

# mc.post("setblock 0 4 0 bedrock")
# set_block(Coordinates, Block)
class Coordinates:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z
    
    def to_str(self):
        return (f'{self.x} {self.y} {self.z}')
        
class Item:
    pass

class Block:
    def __init__(self, namespace=None, id=None):
        self.namespace = namespace
        self.id = id

    def to_str(self):
        return (f'{self.namespace}:{self.id}')
        

class Command:
    def __init__(self, name='', args=[''], usage=""):
        self.name = name
        self.ags = args
        self.usage = usage

    def str_renderer:
        func

# set_block = Command('setblock', [Coordinates, Block, ['destroy', 'keep', 'replace']], "setblock <pos> <block> [destroy|keep|replace]")

def set_block(coords, block):
    mc.post(f'setblock {coords} {block}')


