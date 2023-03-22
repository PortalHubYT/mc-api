import unittest

from shulker.components.Entity import Entity

class TestBlock(unittest.TestCase):
    def test_entity_invalid_descriptor(self):
        with self.assertRaises(ValueError):
            Entity("dog")

    def test_entity_incorrect_descriptor(self):
        with self.assertRaises(ValueError):
            Entity("")


if __name__ == "__main__":
    unittest.main()
