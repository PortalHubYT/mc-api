import unittest

from mc_api.components.Command import Command
from mc_api.components.Block import Block
from mc_api.components.Coordinates import Coordinates
from mc_api.components.BlockHandler import BlockHandler
from mc_api.components.BlockState import BlockState


class TestBlockHandler(unittest.TestCase):
    def test_handler_real_case(self):
        command = Command('setblock', Coordinates(0, 0, 0), Block('bedrock'), BlockHandler('destroy'))

        diff = repr(command)
        test = "setblock 0 0 0 minecraft:bedrock[]{} destroy"
        self.assertEqual(diff, test)

    def test_fill_with_blockstate(self):
        pos1 = Coordinates(0, 4, 0)
        pos2 = Coordinates(10, 4, 10)
        bs = BlockState({"facing": "north", "half": "top"})
        block = Block("oak_stairs", blockstate = bs)

        command = Command('fill', pos1, pos2, block)

        diff = repr(command)
        expected = "fill 0 4 0 10 4 10 minecraft:oak_stairs[facing=north,half=top]{}"
        self.assertEqual(diff, expected)