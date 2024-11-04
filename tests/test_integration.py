# tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.fixture
def setup_test_data():
    # Test data definition
    return [
        {
            "flight_number": "XX1234",
            "departure_city": "BUE",
            "arrival_city": "MAD",
            "departure_datetime": "2024-09-12T12:00:00",
            "arrival_datetime": "2024-09-13T00:00:00",
        },
        {
            "flight_number": "XX2345",
            "departure_city": "MAD",
            "arrival_city": "PMI",
            "departure_datetime": "2024-09-13T02:00:00",
            "arrival_datetime": "2024-09-13T03:00:00",
        },
    ]


def test_integration_journey_search_direct(mock_provider):
    # Integration test for a direct journey from BUE to MAD
    response = client.get(
        "/journeys/search", params={"date": "2024-09-12", "from": "BUE", "to": "MAD"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["connections"] == 1
    assert data[0]["path"][0]["flight_number"] == "XX1234"


def test_integration_journey_search_with_connection(mock_provider):
    # Integration test for a journey with a connection from BUE to PMI
    response = client.get(
        "/journeys/search", params={"date": "2024-09-12", "from": "BUE", "to": "PMI"}
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["connections"] == 2
    assert data[0]["path"][0]["flight_number"] == "XX1234"
    assert data[0]["path"][1]["flight_number"] == "XX2345"


def test_integration_no_journey_found(mock_provider):
    # Integration test for no journeys found from BUE to XXX on a specific date
    response = client.get(
        "/journeys/search", params={"date": "2024-09-12", "from": "BUE", "to": "XXX"}
    )
    assert response.status_code == 404  # assume no values for  "XXX"
