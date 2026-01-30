import pytest
from fastapi.testclient import TestClient
from video_analytics_orchestrator.app.main import app

def test_orchestrator_route():
    client = TestClient(app)
    response = client.post('/orchestrator/', json={'key': 'value'})
    assert response.status_code == 200

# Additional tests for routes