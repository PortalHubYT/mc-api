class Entity:
    def __init__(self, id: str, namespace: str = 'minecraft'):
        self.id = id
        self.namespace = namespace
    
    def __repr__(self):
        return (f'{self.id}:{self.namespace}')