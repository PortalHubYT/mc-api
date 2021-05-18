from .Entity import Entity

class SummonableEntity:
    def __init__(self, entity: Entity):
        self.entity = entity

    def __repr__(self):
        return(f'{self.entity.namespace}:{self.entity.id}')