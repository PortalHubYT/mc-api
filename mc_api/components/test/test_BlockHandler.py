import unittest

from mc_api.components.BlockHandler import BlockHandler, BlockHandlerWrongType
from mc_api.components.Command import Command
from mc_api.components.Block import Block
from mc_api.components.Coordinates import Coordinates

class TestBlockHandler(unittest.TestCase):

    def test_handler_real_case(self):
        diff = Command('setblock', [Coordinates(0, 0, 0), Block('bedrock'), BlockHandler('destroy')]).to_str()
        test = "setblock 0 0 0 minecraft:bedrock destroy"
        self.assertEqual(diff, test)

    def test_handler_destroy(self):
        diff = BlockHandler('destroy').to_str()
        test = "destroy"
        self.assertEqual(diff, test)
    
    def test_handler_replace(self):
        diff = BlockHandler('replace').to_str()
        test = "replace"
        self.assertEqual(diff, test)
    
    def test_handler_keep(self):
        diff = BlockHandler('keep').to_str()
        test = "keep"
        self.assertEqual(diff, test)
    
    def test_handler_hollow(self):
        diff = BlockHandler('hollow').to_str()
        test = "hollow"
        self.assertEqual(diff, test)

    def test_handler_outline(self):
        diff = BlockHandler('outline').to_str()
        test = "outline"
        self.assertEqual(diff, test)

    def test_abritrary_handler(self):
        passed = False
        try:
            BlockHandler('imaginary').to_str()
            passed = False
        except BlockHandlerWrongType:
            passed = True
        self.assertTrue(passed)


if __name__ == '__main__':
    unittest.main()
    