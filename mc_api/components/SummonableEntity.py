from .Entity import Entity

class SummonableEntity:
    """
    Should Summonable be a property of Entity instead of being its own class?
    """

    def __init__(self, entity: Entity):
        self.entity = entity
        self.tags = self.entity.tags

    def define(self, property, value):
        self.entity.add(property, value)   

    def __repr__(self):
        return(f'{self.entity.namespace}:{self.entity.id}')