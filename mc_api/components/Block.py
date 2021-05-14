from .utils import flatten

class Block():
    def __init__(self, id, namespace="minecraft", blockstate=None, metadata=None):
        self.namespace = namespace
        self.id = id

        self.blockstate = blockstate
        self.metadata = metadata
    

    def to_str(self):
        buff = f'{self.namespace}:{self.id}'
        buff+=(flatten(self.blockstate))
        buff+=(flatten(self.metadata))
        return buff