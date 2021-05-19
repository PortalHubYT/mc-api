from mc_api.components import BlockCoordinates
from .base_functions import *

def _advancement(block_coordinates: BlockCoordinates) -> str:
    void_coordinates = BlockCoordinates(block_coordinates.x, -64, block_coordinates.y)

    response = send(f'loot spawn {repr(void_coordinates)} mine {repr(block_coordinates)}')
    response = response.split('/')[-1]

    return response

def advancement(block_coordinates: BlockCoordinates or tuple) -> str:
    """
    with “/loot ... mine <x y z> diamond_pickaxe{Enchantments:[{id:silk_touch,lvl:1}]}”, 
    grab the id from the dropped loot and you’re good to go. There are some blocks this 
    doesn’t apply for, barriers, bedrock, structure/command blocks, end portal frame, 
    but you’ll be able to hard code those your
    """
    # TODO: Add a better implementation of fetching block id
    # TODO: Update this function to implement returning block_state and metadata from the block fetched
    # TODO: (Not Important) Add arguments depth to the loot function

    check_output_channel()

    block_coordinates = format_arg(block_coordinates, BlockCoordinates)

    return _advancement(block_coordinates)

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