from mc_api.components.Coordinates import Coordinates
from mc_api.components import Entity, SummonableEntity, NBT
from .base_functions import *

def _summon(entity: SummonableEntity,
            coords: Coordinates,
            nbt: NBT) -> str:
    
    if coords:
        if nbt:
            response = send('summon', entity, coords, nbt)
        else:
            response = send('summon', entity, coords)
    else:
        response = send('summon', entity)
   
    return response

def summon(entity: SummonableEntity or str,
            coords: Coordinates or tuple = None,
            nbt: NBT or dict = None) -> str:
    """
    If no coords are provided, it defaults to spawning the entity at spawn.
    """
    check_output_channel()

    if type(entity) is str:
        entity = SummonableEntity(Entity(entity))
    
    if coords:
        coords = format_arg(coords, Coordinates)

        if nbt:
            nbt = format_arg(nbt)
    
    else:
        nbt = None

    return _summon(entity, coords, nbt)
    
meta_definition = {
    "summon": {
      "type": "literal",
      "children": {
        "entity": {
          "type": "argument",
          "parser": SummonableEntity,
          "children": {
            "pos": {
              "type": "argument",
              "parser": Coordinates,
              "children": {
                "nbt": {
                  "type": "argument",
                  "parser": NBT,
                  "executable": True
                }
              },
              "executable": True
            }
          },
          "executable": True
        }
      }
    }
}