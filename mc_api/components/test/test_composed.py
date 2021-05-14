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