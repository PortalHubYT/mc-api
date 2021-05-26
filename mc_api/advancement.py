from mc_api.components.Entity import Entity
from mc_api.components import BlockCoordinates, AbstractOption, ResourceLocation
from .base_functions import *

def _advancement(action: AbstractOption,
                entity: Entity,
                option: AbstractOption,
                advancement: ResourceLocation = None,
                criterion: AbstractOption = None) -> str:

    if repr(option) == 'everything':
        response = send('advancement', action, entity, option)
    elif repr(option) == 'only':
        response = send('advancement', action, entity, option, advancement)
        if criterion:
            response = send('advancement', action, entity, option, advancement, criterion)
    else:
        response = send('advancement', action, entity, option, advancement)

    return response

def advancement(action: AbstractOption or str,
                target: Entity or str,
                option: AbstractOption or str,
                advancement: ResourceLocation or str = None,
                criterion: AbstractOption or str = None) -> str:
    """
    grant|revoke

        Specifies whether to add or remove the 
        to-be-specified advancement(s).

    <targets>: entity

        Must be a player name, a target selector or a UUID.
        And the target selector must be of player type.
        Specifies one player or more.

    <advancement>: resource_location

        Must be a namespaced ID.
        Specifies a valid namespaced id of the advancement to
        target.

    <criterion>: string

        Must be a string.
        Specifies a valid criterion of the advancement to manipulate.
        The command defaults to the entire advancement.
        If specified, the command refers to merely the criterion 
        and not the entire advancement.
    """
    check_output_channel()

    action = format_arg(action, AbstractOption)
    target = format_arg(target, Entity)
    option = format_arg(option, AbstractOption)

    if type(advancement) is str:
        if ':' in advancement:
            advancement = advancement.split(':')
            advancement = ResourceLocation(advancement[1], namespace=advancement[0])
        else:
            advancement = format_arg(advancement, ResourceLocation)
    
    if repr(option) != 'only':
        criterion = None
    else:
        criterion = format_arg(criterion, AbstractOption)
        
    return _advancement(action, target, option, advancement, criterion)

meta_definition = {
    "advancement": {
      "type": "literal",
      "children": {
        "grant": {
          "type": "literal",
          "children": {
            "targets": {
              "type": "argument",
              "parser": "minecraft:entity",
              "properties": {
                "amount": "multiple",
                "type": "players"
              },
              "children": {
                "everything": {
                  "type": "literal",
                  "executable": True
                },
                "from": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "executable": True
                    }
                  }
                },
                "only": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "children": {
                        "criterion": {
                          "type": "argument",
                          "parser": "brigadier:string",
                          "properties": {
                            "type": "greedy"
                          },
                          "executable": True
                        }
                      },
                      "executable": True
                    }
                  }
                },
                "through": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "executable": True
                    }
                  }
                },
                "until": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "executable": True
                    }
                  }
                }
              }
            }
          }
        },
        "revoke": {
          "type": "literal",
          "children": {
            "targets": {
              "type": "argument",
              "parser": "minecraft:entity",
              "properties": {
                "amount": "multiple",
                "type": "players"
              },
              "children": {
                "everything": {
                  "type": "literal",
                  "executable": True
                },
                "from": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "executable": True
                    }
                  }
                },
                "only": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "children": {
                        "criterion": {
                          "type": "argument",
                          "parser": "brigadier:string",
                          "properties": {
                            "type": "greedy"
                          },
                          "executable": True
                        }
                      },
                      "executable": True
                    }
                  }
                },
                "through": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "executable": True
                    }
                  }
                },
                "until": {
                  "type": "literal",
                  "children": {
                    "advancement": {
                      "type": "argument",
                      "parser": "minecraft:resource_location",
                      "executable": True
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
}