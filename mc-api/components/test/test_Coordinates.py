import unittest
from components.Coordinates import Coordinates

class TestCoordinates(unittest.TestCase):

    def test_zeros(self):
        c = Coordinates(0, 0, 0)

        ret = c.to_str()
        self.assertEqual(ret, "0 0 0")
        self.assertEqual(ret, "0 0 0")
        self.assertEqual(ret, "0 0 0")
        self.assertEqual(ret, "0 0 0")
        self.assertEqual(ret, "0 0 0")


if __name__ == '__main__':
    unittest.main()
    