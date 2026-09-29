import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    # Guard against cross-test leakage since `activities` is mutated in place.
    original_state = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(original_state)
