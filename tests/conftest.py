from copy import deepcopy
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


PRISTINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities() -> Generator[None, None, None]:
    """Keep mutations to the in-memory activity data isolated to each test."""
    activities.clear()
    activities.update(deepcopy(PRISTINE_ACTIVITIES))

    yield

    activities.clear()
    activities.update(deepcopy(PRISTINE_ACTIVITIES))


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client
