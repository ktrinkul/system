import unittest
from .database import DatabaseHandler

class TestDatabaseHandler(unittest.TestCase):
    def test_crud_operations(self):
        db_handler = DatabaseHandler()
        db_handler.create(data)
        fetched_data = db_handler.read(id)
        self.assertEqual(fetched_data, expected_data)

    # Additional tests here

if __name__ == '__main__':
    unittest.main()