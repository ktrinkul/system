import unittest
from fastapi.testclient import TestClient
from .main import app

class TestScenarioRouter(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_scenario(self):
        response = self.client.get('/scenario/1/')
        self.assertEqual(response.status_code, 200)

    # Additional tests here

if __name__ == '__main__':
    unittest.main()