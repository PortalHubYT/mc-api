import unittest

from mc_api.components.Message import Message
from mc_api.components.TargetSelector import TargetSelector


class TestBlock(unittest.TestCase):
    def test_message_only_str(self):
        name = "Natasha"
        msg = Message("hey this is", name)

        diff = str(msg)
        test = "hey this is Natasha"
        self.assertEqual(diff, test)

    def test_message_only_TargetSelector(self):
        ts = TargetSelector("p", {"tag": "dog"})
        msg = Message(ts)

        diff = str(msg)
        test = "@p[tag=dog]"
        self.assertEqual(diff, test)

    def test_message_mixed_args(self):
        ts = TargetSelector("p", {"tag": "dog"})
        msg = Message("hey this is", ts, "lol")

        diff = str(msg)
        test = "hey this is @p[tag=dog] lol"
        self.assertEqual(diff, test)

    def test_message_invalid_args(self):
        with self.assertRaises(ValueError):
            msg = Message(["this is", "an invalid", "format"])
            str(msg)


if __name__ == "__main__":
    unittest.main()
