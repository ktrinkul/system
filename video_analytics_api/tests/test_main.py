import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_main_function(self):
        try:
            main()  # Call main and ensure no exceptions raised
        except Exception:
            self.fail('main() raised an exception')

if __name__ == '__main__':
    unittest.main()