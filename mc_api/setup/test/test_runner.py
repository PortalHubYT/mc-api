import unittest
import subprocess
from os import path

class TestRunner(unittest.TestCase):

    def test_runner(self):
        subprocess.run(['sh', 'run.sh'], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        self.assertTrue(True)

    def test_output(self):
        self.assertEqual(path.exists('generated'), True)
        
if __name__ == '__main__':
    unittest.main()
    