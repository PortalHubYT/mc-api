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
    # TODO: (Not Important) Add depth to the loot function 
    
    def __init__(self, block_coordinates: BlockCoordinates):
        self.check_interface()
        self.block_coordinates = self.format_arg(block_coordinates, BlockCoordinates)

        self.void_coordinates = BlockCoordinates(self.block_coordinates.x, -64, self.block_coordinates.y)

        self.response = self.send(f'loot spawn {self.void_coordinates.to_str()} mine {self.block_coordinates.to_str()}')
        self.response = self.response.split('/')[-1]


def get_block(block_coordinates: BlockCoordinates) -> str: 
    command = GetBlock(block_coordinates)
    return command.response

class UnexpectedReturn(Exception):
    pass