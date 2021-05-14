from container_connecter import ConnectServerInstance

mc = ConnectServerInstance()

class Metadata:
    def __init__(self, value):
        self.value = value

    def to_str(self):
        return (f'{self.value}')

class Command:
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def to_str(self):
        #TO-DO: Test this, that args correctly unpack
        return(f'{self.name} {" ".join([arg.to_str() for arg in self.args])}')

# setblock <pos> <block> [destroy|keep|replace]
def setblock(coords, block, block_handler=REPLACE): 
    command = Command("setblock", [coords, block, block_handler])
    mc.post(command.to_str())

# fill <from> <to> <block> replace [<filter>]
# fill <from> <to> <block> [destroy|hollow|keep|outline|replace]
def fill(coords1, coords2, block, block_handler=None, filter=None):
    if block_handler is None:
        command = Command("fill", [coords1, coords2, block])
    elif block_handler == REPLACE:
        if filter:
            command = Command("fill", [coords1, coords2, block, block_handler, filter])
        else:
            command = Command("fill", [coords1, coords2, block, block_handler])
    else:
        command = Command("fill", [coords1, coords2, block, block_handler])

    mc.post(command.to_str())
