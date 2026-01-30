import pytest
from video_analytics_orchestrator.app.schemas import YourSchema

def test_schema_validation():
    schema = YourSchema()
    valid_data = {'key': 'value'}
    assert schema.validate(valid_data) is True

# Additional tests for schemas