import unittest

from mc_api.components.Block import Block
from mc_api.components.BlockState import BlockState

class TestBlock(unittest.TestCase):

    def test_bedrock(self):
        diff = repr(Block("bedrock"))
        test = "minecraft:bedrock"
        self.assertEqual(diff, test)

    def test_namespace(self):
        diff = repr(Block("op_block", "mod"))
        test = "mod:op_block"
        self.assertEqual(diff, test)
    
    def test_simple_blockstate(self):
        b_state = BlockState('facing', 'north')
        diff = repr(Block("op_block", "mod", b_state))
        test = "mod:op_block[facing=north]"
        self.assertEqual(diff, test)

    def test_double_blockstate(self):
        bs_facing = BlockState('facing', 'north')
        bs_half = BlockState('half', 'top')

        diff = repr(Block("op_block", "mod", [bs_facing, bs_half]))
        test = "mod:op_block[facing=north,half=top]"
        self.assertEqual(diff, test)
    
    def test_empty_blockstate(self):

        diff = repr(Block("op_block", "mod", blockstate=[]))
        test = "mod:op_block"
        self.assertEqual(diff, test)
    
    def test_empty(self):
        with self.assertRaises(ValueError):
            a = Block("")




if __name__ == '__main__':
    unittest.main()