from typing import Union

# components


class Block:
    ...  # ok + test


class BlockState:
    ...  # ok + test


class NBT:
    ...  # ok + test


class BlockCoordinates:
    ...  # ok + test


class Coordinates:
    ...  # ok + test


class BlockHandler:
    ...  # ok + test


class Zone:
    ...  # ok + test


class Command:
    ...  # ok + test


class Entity:
    ...  # ok + test


class TargetSelector:
    ...  # ok + test


class Message:
    ...  # ok + test


# top level functions:


def set_text():
    ...  # ok


def set_block():
    ...  # ok


def set_zone() -> bool:
    ...  # ok


def get_block(coords: Union[BlockCoordinates, Coordinates, tuple]) -> Block:
    """
    Returns a Block component, which contains its representation
    using repr(Block)

    # TODO: Double-check that any coords type can be used here
    """


def get_blocks(zone: Zone) -> list:
    """
    # TODO: its existence is problematic, should it be a method of Zone instead?

    Get the blocks in a rectangular zone

    It returns a tuple containing the blocks
    the zone represents
    """


def get_player(selector: Union[TargetSelector, str]) -> Player:
    """
    Fill an instance of the component Player with the
    NBT tags fetched from the Selector component
    or the str passed, evaluated as the name of the player to be fetched.

    # TODO: Use /data get entity wrapped in an execute
    """


def get_players(selector: TargetSelector = "@a") -> list:
    """
    Fill a list with the players currently
    connected on the server. The list will be populated
    with Player (component) instances.

    A custom selector can be used to filter more accurately.
    By default, selects all the player online.

    # TODO: Use /data get entity wrapped in an execute
    """


def get_entity(selector: TargetSelector) -> Entity:
    """
    Returns an Entity instance populated with the NBT
    tags fetched depending on the selector.

    # TODO: add limit=1 if not provided since this is get_entity
    # TODO: Use /data get entity wrapped in an execute
    """


def get_entities(selector: TargetSelector = None) -> list:
    ...


def summon_entity(entity):
    ...


def summom_particles():
    ...


def say():
    ...


def whisper():
    ...


def title():
    ...


def teleport():
    ...  # tp


def ban():
    ...


def kick():
    ...


def kill():
    ...


def op():
    ...


def set_gamemode():
    ...


def whitelist():
    ...


def set_difficulty():
    ...


def inventory_give():
    ...


def inventory_remove():
    ...


def give_effect():
    ...


def remove_effect():
    ...


def play_sound():
    ...


def weather():
    ...


def gamerule():
    ...


#############
# super functions
###############

# def play_midi(): ...

# misc
