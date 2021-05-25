from mc_api.components.BlockCoordinates import BlockCoordinates
import unittest

from mc_api.components.Command import Command
from mc_api.components.Block import Block
from mc_api.components.BlockCoordinates import BlockCoordinates
from mc_api.components.BlockHandler import BlockHandler
from mc_api.components.NBT import NBT
from mc_api.components.BlockState import BlockState

class TestCommand(unittest.TestCase):

    def test_command_without_args(self):
        command = Command("tps")

        diff = repr(command)
        test = "tps"
        self.assertEqual(diff, test)
    
    def test_command_with_args(self):
        block = Block('bedrock')
        block_coords = BlockCoordinates(0, 0, 0)
        bs = BlockState({"snowy": True})
        tags = NBT({"Fire": 4})
        bh = BlockHandler("replace")
        replace_block = Block('grass_block')

        block.blockstate = bs
        block.nbt = tags

        command = Command("setblock", block_coords, block, bh, replace_block)

        diff = repr(command)
        test = "setblock 0 0 0 minecraft:bedrock[snowy=true]{Fire:4} replace minecraft:grass_block[]{}"
        self.assertEqual(diff, test)
    


if __name__ == '__main__':
    unittest.main()
    