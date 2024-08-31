import pytest
from fastapi.testclient import TestClient

from social_network_simulation.api import app


@pytest.fixture
def client():
    api_client = TestClient(app)
    return api_client