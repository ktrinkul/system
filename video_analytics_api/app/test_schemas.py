import unittest
from .schemas import YourSchema

class TestYourSchema(unittest.TestCase):
    def test_schema_validation(self):
        schema_instance = YourSchema()
        self.assertTrue(schema_instance.validate({'key': 'value'}))

    # Additional tests here

if __name__ == '__main__':
    unittest.main()