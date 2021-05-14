import unittest

try:
    from mc_api.setup.runner import Runner
except ModuleNotFoundError:
    from runner import Runner

class TestRunner(unittest.TestCase):

    def test_run(self):
        tasks = Runner()
        tasks.run()
 
if __name__ == '__main__':
    unittest.main()
    