from .NBTTags import NBTTags

class Entity:
    def __init__(self, id: str, namespace: str = 'minecraft'):
        self.id = id
        self.namespace = namespace

        self.tags = NBTTags()

    def define(self, property, value):
        self.tags.add(property, value)
    
    def __repr__(self):
        return (f'{self.id}:{self.namespace}')