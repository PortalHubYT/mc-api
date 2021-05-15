import unittest

from mc_api.components.Command import Command
from mc_api.components.Block import Block
from mc_api.components.Coordinates import Coordinates
from mc_api.components.BlockHandler import BlockHandler


class TestBlockHandler(unittest.TestCase):
    def test_handler_real_case(self):
        diff = Command('setblock', Coordinates(0, 0, 0), Block('bedrock'), BlockHandler('destroy')).to_str()
        test = "setblock 0 0 0 minecraft:bedrock destroy"
        self.assertEqual(diff, test)

    def test_fill_wblockstate(self):
        pos1 = Coordinates(0, 4, 0)
        pos2 = Coordinates(10, 4, 10)
        facing = BlockState("facing", "north")
        half = BlockState("half", "top")
        block = Block("oak_stairs", blockstate = [facing, half])

        command = Command('fill', pos1, pos2, block)
        expected = "fill 0 4 0 10 4 10 minecraft:oak_stairs[facing=north,half=top]"
        self.assertEqual(command.to_str(), expected)