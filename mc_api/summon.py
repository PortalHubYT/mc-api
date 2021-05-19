from mc_api.components.Coordinates import Coordinates
from mc_api.components import Entity, SummonableEntity, NBTTags
from .base_functions import *

def _summon(entity: SummonableEntity,
            coords: Coordinates,
            metadata: NBTTags) -> str:
    
    if coords:
        if metadata:
            response = send('summon', entity, coords, metadata)
        else:
            response = send('summon', entity, coords)
    else:
        response = send('summon', entity)
   
    return response

def summon(entity: SummonableEntity or str,
            coords: Coordinates or tuple = None,
            metadata: NBTTags or dict = None) -> str:
    """
    If no coords are provided, it defaults to spawning the entity at spawn.
    """
    check_output_channel()

    if type(entity) is str:
        entity = SummonableEntity(Entity(entity))
    
    if coords:
        coords = format_arg(coords, Coordinates)

        if metadata:
            metadata = format_arg(metadata)
    
    else:
        metadata = None

    return _summon(entity, coords, metadata)
    
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
                  "parser": NBTTags,
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