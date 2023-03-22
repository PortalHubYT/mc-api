import json
import os

from typing import Union

from shulker.components.BlockCoordinates import BlockCoordinates
from shulker.components.NBT import NBT
from shulker.components.Coordinates import Coordinates
from shulker.components.Entity import Entity

from shulker.functions.base_functions import *


def meta_summon(entity: str, coords: BlockCoordinates, nbt_data: NBT) -> str:
    return f"summon {entity} {coords} {nbt_data}"


def summon(
    entity: Union[Entity, str],
    coords: Union[BlockCoordinates, Coordinates, tuple],
    nbt_data: Union[NBT, dict, str, None] = None
) -> str:
    """
    Summons an entity at coords, can be provided nbt_data
    """

    check_output_channel()
        
    if type(entity) is str:
      entity = Entity(entity)

    coords = format_arg(coords, Coordinates)
        
    cmd = meta_summon(entity.descriptor, coords, entity.nbt)

    status = post(cmd)
    
    return status
