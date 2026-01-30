import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestScenarioRouter(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_create_scenario(self):
        response = self.client.post('/scenario/', json={...})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()