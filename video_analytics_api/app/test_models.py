import unittest
from .models import YourModel

class TestYourModel(unittest.TestCase):
    def test_model_creation(self):
        model_instance = YourModel(param1='value1')
        self.assertEqual(model_instance.param1, 'value1')

    # Additional tests here

if __name__ == '__main__':
    unittest.main()