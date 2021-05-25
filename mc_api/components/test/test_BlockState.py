import unittest

from mc_api.components.BlockState import BlockState
from mc_api.components.Block import Block

class TestBlock(unittest.TestCase):

    def test_blockstate_without_args(self):
        bs = BlockState()

        diff = repr(bs)
        test = "[]"
        self.assertEqual(diff, test)
    
    def test_blockstate_without_attrs(self):
        b = Block('dirt')

        diff = repr(b.blockstate)
        test = "[]"
        self.assertEqual(diff, test)
    
    def test_blockstate_without_args_passed_to_Block(self):
        bs = BlockState()
        b = Block('dirt', blockstate=bs)

        diff = repr(b.blockstate)
        test = '[]'
        self.assertEqual(diff, test)

    def test_blockstate_without_args_attributed_to_Block(self):
        bs = BlockState()
        b = Block('dirt')

        b.blockstate = bs

        diff = repr(b.blockstate)
        test = '[]'
        self.assertEqual(diff, test)

    def test_blockstate_with_arg(self):
        bs = BlockState({"snowy": True})

        diff = repr(bs)
        test = '[snowy=true]'
        self.assertEqual(diff, test)
    
    def test_blockstate_with_args(self):
        bs = BlockState({"snowy": True, "facing": "north"})

        diff = repr(bs)
        test = '[facing=north,snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_via_attr(self):
        bs = BlockState()
        bs.snowy = True

        diff = repr(bs)
        test = '[snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_via_attrs(self):
        bs = BlockState()
        bs.snowy = True
        bs.facing = "north"

        diff = repr(bs)
        test = '[facing=north,snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_with_arg_passed_to_Block(self):
        bs = BlockState({"snowy": True})
        b = Block('dirt', blockstate=bs)

        diff = repr(b.blockstate)
        test = '[snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_with_args_passed_to_Block(self):
        bs = BlockState({"snowy": True, "facing": "north"})
        b = Block('dirt', blockstate=bs)

        diff = repr(b.blockstate)
        test = '[facing=north,snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_via_attr_through_Block(self):
        b = Block('dirt')
        b.blockstate.snowy = True

        diff = repr(b.blockstate)
        test = '[snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_via_attrs_through_Block(self):
        b = Block('dirt')
        b.blockstate.snowy = True
        b.blockstate.facing = 'north'

        diff = repr(b.blockstate)
        test = '[facing=north,snowy=true]'
        self.assertEqual(diff, test)

    def test_blockstate_mixed_attrs_and_args_through_Block(self):
        bs = BlockState({"snowy": True, "dancing": "well"})
        b = Block('dirt')
        b.blockstate = bs
        b.blockstate.facing = 'north'

        diff = repr(b.blockstate)
        test = '[dancing=well,facing=north,snowy=true]'
        self.assertEqual(diff, test)