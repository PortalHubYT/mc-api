from mc_api.components import CustomFunction, Block, Subcommand, BlockCoordinates

class TestBlock(CustomFunction):
    def __init__(self, block_coordinates: BlockCoordinates, block: Block):
        self.check_interface()
        self.block_coordinates = self.format_arg(block_coordinates, BlockCoordinates)
        self.block = self.format_arg(block, Block)
        
        self.subcommand = Subcommand('if', 'block')

        self.response = self.send('execute', self.subcommand, 
                                    self.block_coordinates, self.block)

        self.status = self.execute_check(self.response)

        if self.status is str:
            self.unexpected_status(__file__, self.status, self.command)


def test_block(block_coordinates: BlockCoordinates or tuple, 
                block: Block or str) -> bool: 

    command = TestBlock(block_coordinates, block)
    return command.status

class UnexpectedReturn(Exception):
    pass