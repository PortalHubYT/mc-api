import unittest
from components.Block import Block

class TestBlock(unittest.TestCase):

    def test_bedrock(self):
        block = Block("bedrock")
        diff = block.to_str()
        test = "minecraft:bedrock"
        self.assertEqual(diff, test)

    def test_namespace(self):
        block = Block("dirt", "mod")
        diff = block.to_str()
        test = "mod:dirt"
        self.asserEqual(diff, test)

if __name__ == '__main__':
    unittest.main()