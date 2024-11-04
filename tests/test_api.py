from fastapi.testclient import TestClient
from core.services.journey_search_service import JourneySearchService
from main import app
import pytest

client = TestClient(app)


# Override de la dependencia en los tests de API
@pytest.fixture(autouse=True)
def override_journey_search_service(mock_provider):
    app.dependency_overrides[JourneySearchService] = lambda: JourneySearchService(
        mock_provider
    )
    yield
    app.dependency_overrides = {}


def test_search_journeys_direct():
    response = client.get(
        "/journeys/search", params={"date": "2024-09-12", "from": "BUE", "to": "MAD"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["connections"] == 1
    assert data[0]["path"][0]["flight_number"] == "XX1234"


def test_search_journeys_with_connection():
    response = client.get(
        "/journeys/search", params={"date": "2024-09-12", "from": "BUE", "to": "PMI"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["connections"] == 2
    assert data[0]["path"][0]["flight_number"] == "XX1234"
    assert data[0]["path"][1]["flight_number"] == "XX2345"


def test_no_journey_found():
    response = client.get(
        "/journeys/search", params={"date": "2024-09-12", "from": "BUE", "to": "XXX"}
    )
    assert response.status_code == 404  # asume no values for  "XXX"
