from mc_api.components import CustomFunction, Block, BlockCoordinates

class SetBlock(CustomFunction):
    def __init__(self, block_coordinates: BlockCoordinates, block: Block, interface=None) -> bool:
        self.interface = self.check_interface(interface, __file__)
        self.block_coordinates = self.format_arg(block_coordinates, BlockCoordinates)
        self.block = self.format_arg(block, Block)
    
        self.response = self.send('setblock', self.block_coordinates, self.block)
        self.status = self.execute_check(self.response)

        if self.status is str:
            raise UnexpectedReturn(f'The execute command in testblock() didn\'t properly function and returned: "{self.status}" with the command "{self.command}"')


def set_block(block_coordinates: BlockCoordinates, block: Block, interface=None): 
    return SetBlock(block_coordinates, block, interface).status

class UnexpectedReturn(Exception):
    pass