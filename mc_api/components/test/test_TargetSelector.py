import unittest

from mc_api.components.TargetSelector import TargetSelector
from mc_api.components.TargetSelector import IncorrectTargetSelectorIdentifier, IncorrectTargetSelectorArgumentsType, InvalidTargetSelectorArgumentKey

class TestBlock(unittest.TestCase):

    def test_targetselector_p_option(self):
        ts = TargetSelector('p')

        diff = repr(ts)
        test = "@p[]"
        self.assertEqual(diff, test)

    def test_targetselector_a_option(self):
        ts = TargetSelector('a')

        diff = repr(ts)
        test = "@a[]"
        self.assertEqual(diff, test)
    
    def test_targetselector_r_option(self):
        ts = TargetSelector('r')

        diff = repr(ts)
        test = "@r[]"
        self.assertEqual(diff, test)
    
    def test_targetselector_s_option(self):
        ts = TargetSelector('s')

        diff = repr(ts)
        test = "@s[]"
        self.assertEqual(diff, test)
    
    def test_targetselector_e_option(self):
        ts = TargetSelector('e')

        diff = repr(ts)
        test = "@e[]"
        self.assertEqual(diff, test)

    def test_targetselector_invalid_option(self):
        with self.assertRaises(IncorrectTargetSelectorIdentifier):
            TargetSelector('f')

    def test_targetselector_with_no_arguments(self):
        ts = TargetSelector('p', {})

        diff = repr(ts)
        test = "@p[]"
        self.assertEqual(diff, test)

    def test_targetselector_with_argument(self):
        ts = TargetSelector('p', {"team": "french"})

        diff = repr(ts)
        test = "@p[team=french]"
        self.assertEqual(diff, test)

    def test_targetselector_with_arguments(self):
        ts = TargetSelector('p', {"team": "french", "tag": "baguette"})

        diff = repr(ts)
        test = "@p[team=french,tag=baguette]"
        self.assertEqual(diff, test)

    def test_targetselector_with_arguments_listed(self):
        ts = TargetSelector('p', {"team": "french", "tag": ["baguette", "farine"]})

        diff = repr(ts)
        test = "@p[team=french,tag=baguette,tag=farine]"
        self.assertEqual(diff, test)

    def test_targetselector_with_invalid_arguments(self):
        with self.assertRaises(InvalidTargetSelectorArgumentKey):
            repr(TargetSelector('p', {"totem": 5, "tag": "baguette"}))

    def test_targetselector_with_invalid_argument_type(self):
        with self.assertRaises(IncorrectTargetSelectorArgumentsType):
            repr(TargetSelector('p', ['totem', 'tag', 5]))

if __name__ == '__main__':
    unittest.main()