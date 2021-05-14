import unittest

from mc_api.components.Block import Block

class TestBlock(unittest.TestCase):

    def test_bedrock(self):
        diff = Block("bedrock").to_str()
        test = "minecraft:bedrock"
        self.assertEqual(diff, test)

    def test_namespace(self):
        diff = Block("op_block", "mod").to_str()
        test = "mod:op_block"
        self.assertEqual(diff, test)

if __name__ == '__main__':
    unittest.main()