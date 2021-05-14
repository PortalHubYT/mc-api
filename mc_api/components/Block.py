from mc_api.components.BlockState import BlockState
from .utils import flatten
from .BlockState import BlockState

class Block():
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
        
        print(buff)
        return buff

        buff += flatten(self.blockstate)
        buff += flatten(self.metadata)
        return buff