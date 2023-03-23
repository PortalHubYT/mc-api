import unittest

from shulker.components.Block import Block
from shulker.components.BlockZone import BlockZone
from shulker.components.BlockCoordinates import BlockCoordinates
from shulker.components.BlockHandler import BlockHandler

from shulker.functions.default import meta_set_zone


class TestBlock(unittest.TestCase):
    def test_set_zone(self):
        coords = BlockCoordinates(0, 0, 0)
        coords2 = BlockCoordinates(10, 10, 10)
        zone = BlockZone(coords, coords2)
        block = Block("bedrock")
        filter = Block("sponge")
        handler = BlockHandler("hollow")

        diff = meta_set_zone(zone, block, handler, filter)
        test = "fill 0 0 0 10 10 10 minecraft:bedrock hollow"
        self.assertEqual(diff, test)

    def test_set_zone_replace(self):
        coords = BlockCoordinates(0, 0, 0)
        coords2 = BlockCoordinates(10, 10, 10)
        zone = BlockZone(coords, coords2)
        block = Block("bedrock")
        filter = Block("sponge")
        handler = BlockHandler("replace")

        diff = meta_set_zone(zone, block, handler, filter)
        test = "fill 0 0 0 10 10 10 minecraft:bedrock replace minecraft:sponge"
        self.assertEqual(diff, test)

    def test_set_zone_no_handler(self):
        coords = BlockCoordinates(0, 0, 0)
        coords2 = BlockCoordinates(10, 10, 10)
        zone = BlockZone(coords, coords2)
        block = Block("bedrock")
        handler = BlockHandler()

        diff = meta_set_zone(zone, block, handler)
        test = "fill 0 0 0 10 10 10 minecraft:bedrock replace"
        self.assertEqual(diff, test)


if __name__ == "__main__":
    unittest.main()
