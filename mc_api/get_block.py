from mc_api.components import CustomFunction, Block, BlockCoordinates

class GetBlock(CustomFunction):
    """
    with “/loot ... mine <x y z> diamond_pickaxe{Enchantments:[{id:silk_touch,lvl:1}]}”, 
    grab the id from the dropped loot and you’re good to go. There are some blocks this 
    doesn’t apply for, barriers, bedrock, structure/command blocks, end portal frame, 
    but you’ll be able to hard code those yourself.
    """
    def __init__(self, block_coordinates: BlockCoordinates, interface=None) -> bool:
        self.interface = self.check_interface(interface, __file__)
        self.block_coordinates = self.format_arg(block_coordinates, BlockCoordinates)
    
        self.response = self.send('setblock', self.block_coordinates, self.block)
        self.status = self.execute_check(self.response)

        if self.status is str:
            raise UnexpectedReturn(f'The execute command in testblock() didn\'t properly function and returned: "{self.status}" with the command "{self.command}"')


def get_block(block_coordinates: BlockCoordinates, interface=None): 
    return GetBlock(block_coordinates, interface).status

class UnexpectedReturn(Exception):
    pass