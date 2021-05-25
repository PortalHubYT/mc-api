import unittest

from mc_api.components.Coordinates import Coordinates, WrongCaretNotation

class TestCoordinates(unittest.TestCase):

    def test_coords_zeros(self):
        coords = Coordinates(0, 0, 0)

        diff = repr(coords)
        test = "0 0 0"
        self.assertEqual(diff, test)
    
    def test_coords_tilde(self):
        coords = Coordinates('~', '~', '~')

        diff = repr(coords)
        test = "~ ~ ~"
        self.assertEqual(diff, test)

    def test_coords_tilde_mixed(self):
        coords = Coordinates('~5', 0, '~-10')

        diff = repr(coords)
        test = "~5 0 ~-10"
        self.assertEqual(diff, test)

    def test_coords_caret(self):
        coords = Coordinates('^', '^', '^')

        diff = repr(coords)
        test = "^ ^ ^"
        self.assertEqual(diff, test)

    def test_coords_caret_mixed(self):
        coords = Coordinates('^5', '^-10', '^')

        diff = repr(coords)
        test = "^5 ^-10 ^"
        self.assertEqual(diff, test)

    def test_coords_caret_wrong(self):
        coords = Coordinates(5, '^', '^')

        with self.assertRaises(WrongCaretNotation): 
            repr(coords)

if __name__ == '__main__':
    unittest.main()
    