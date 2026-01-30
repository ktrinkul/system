import unittest
from app.schemas import YourSchema

class TestYourSchema(unittest.TestCase):

    def test_valid_data(self):
        valid_data = {...}
        schema = YourSchema()
        result = schema.load(valid_data)
        self.assertEqual(result, valid_data)

    def test_invalid_data(self):
        invalid_data = {...}
        schema = YourSchema()
        with self.assertRaises(ValidationError):
            schema.load(invalid_data)

if __name__ == '__main__':
    unittest.main()