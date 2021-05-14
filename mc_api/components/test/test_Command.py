import unittest

from mc_api.components.Command import Command
from mc_api.components.Block import Block
from mc_api.components.Coordinates import Coordinates

class TestCommand(unittest.TestCase):

    def test_command_without_args(self):
        diff = Command("tps").to_str()
        test = "tps"
        self.assertEqual(diff, test)
    
    def test_command_with_args(self):
        diff = Command("setblock", [Coordinates(0, 0, 0), Block("bedrock")]).to_str()
        test = "setblock 0 0 0 minecraft:bedrock"
        self.assertEqual(diff, test)
        
if __name__ == '__main__':
    unittest.main()
    