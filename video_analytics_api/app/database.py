import unittest
from app.database import Database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()

    def test_crud_operations(self):
        self.db.create(...)
        result = self.db.read(...)
        self.assertIsNotNone(result)
        self.db.update(...)
        self.db.delete(...)

if __name__ == '__main__':
    unittest.main()