from mc_api.components import CustomFunction, BlockCoordinates

class GetBlock(CustomFunction):
    """
    with “/loot ... mine <x y z> diamond_pickaxe{Enchantments:[{id:silk_touch,lvl:1}]}”, 
    grab the id from the dropped loot and you’re good to go. There are some blocks this 
    doesn’t apply for, barriers, bedrock, structure/command blocks, end portal frame, 
    but you’ll be able to hard code those yourself.
    """
    # TODO: Add a better implementation of fetching block id
    # TODO: Update this function to implement returning block_state and metadata from the block fetched
    
    def __init__(self, block_coordinates: BlockCoordinates, interface=None) -> bool:
        self.interface = self.check_interface(interface, __file__)
        self.block_coordinates = self.format_arg(block_coordinates, BlockCoordinates)
    
        self.response = self.send(f'loot spawn {self.block_coordinates.to_str()} mine {self.block_coordinates.to_str()}')
        self.response = self.response.split('/')[-1]


def get_block(block_coordinates: BlockCoordinates, interface=None): 
    return GetBlock(block_coordinates, interface).response

class UnexpectedReturn(Exception):
    pass