import pytest
from video_analytics_orchestrator.app.models import YourModel

def test_model_creation():
    model_instance = YourModel(param1='value1')
    assert model_instance.param1 == 'value1'

# Additional tests for models