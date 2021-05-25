import unittest

from mc_api.components.BlockHandler import BlockHandler, BlockHandlerWrongType
from mc_api.components.Block import Block

class TestBlockHandler(unittest.TestCase):

    def test_handler_destroy(self):
        bh = BlockHandler('destroy')

        diff = repr(bh)
        test = "destroy"
        self.assertEqual(diff, test)
    
    def test_handler_replace(self):
        bh = BlockHandler('replace')

        diff = repr(bh)
        test = "replace"
        self.assertEqual(diff, test)
    
    def test_handler_keep(self):
        bh = BlockHandler('keep')

        diff = repr(bh)
        test = "keep"
        self.assertEqual(diff, test)
    
    def test_handler_hollow(self):
        bh = BlockHandler('hollow')

        diff = repr(bh)
        test = "hollow"
        self.assertEqual(diff, test)

    def test_handler_outline(self):
        bh = BlockHandler('outline')

        diff = repr(bh)
        test = "outline"
        self.assertEqual(diff, test)
    
    def test_handler_default(self):
        bh = BlockHandler()

        diff = repr(bh)
        test = "replace"
        self.assertEqual(diff, test)

    # This tests that BlockHandler correctly throws an exception on wrong BlockHandler type
    def test_abritrary_handler(self):
        passed = False
        try:
            bh = BlockHandler('imaginary')
            repr(bh)
            passed = False
        except BlockHandlerWrongType:
            passed = True
        self.assertTrue(passed)


if __name__ == '__main__':
    unittest.main()
    