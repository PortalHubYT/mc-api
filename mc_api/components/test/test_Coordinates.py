import unittest

from mc_api.components.Coordinates import Coordinates

class TestCoordinates(unittest.TestCase):

    def test_zeros(self):
        diff = Coordinates(0, 0, 0).to_str()
        test = "0 0 0"
        self.assertEqual(diff, test)


if __name__ == '__main__':
    unittest.main()
    