from mc_api.components import BlockState, Metadata

class Block:
    def __init__(self, id, namespace="minecraft"):
        self.namespace = namespace
        self.id = id

        self.blockstate = BlockState.BlockState()
        #self.metadata = Metadata.Metadata()
    
    def to_str(self):
        return (f'{self.namespace}:{self.id}{self.blockstate.to_str()}{self.metadata.to_str()}')