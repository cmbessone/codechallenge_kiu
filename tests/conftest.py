# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from typing import List
from main import app
from core.domain.models import FlightEvent
from core.interface.flight_event_provider import FlightEventProvider
from core.services.journey_search_service import JourneySearchService
from controllers.journey_controller import get_journey_search_service


# Mock provider class that implements the FlightEventProvider interface
class MockFlightEventProvider(FlightEventProvider):
    def __init__(self, flight_events: List[FlightEvent]):
        self._flight_events = flight_events

    def get_flight_events(self) -> List[FlightEvent]:
        return self._flight_events


# Sample flight events fixture
@pytest.fixture
def sample_flight_events():
    return [
        FlightEvent(
            flight_number="XX1234",
            departure_city="BUE",
            arrival_city="MAD",
            departure_datetime=datetime(2024, 9, 12, 12, 0),
            arrival_datetime=datetime(2024, 9, 13, 0, 0),
        ),
        FlightEvent(
            flight_number="XX2345",
            departure_city="MAD",
            arrival_city="PMI",
            departure_datetime=datetime(2024, 9, 13, 2, 0),
            arrival_datetime=datetime(2024, 9, 13, 3, 0),
        ),
    ]


# Fixture to provide a mock FlightEventProvider for general tests
@pytest.fixture
def mock_provider(sample_flight_events):
    return MockFlightEventProvider(sample_flight_events)


# Fixture specifically for testing journeys that exceed max duration constraints
@pytest.fixture
def mock_provider_exceeding_max_duration():
    flight_events = [
        FlightEvent(
            flight_number="XX1234",
            departure_city="BUE",
            arrival_city="MAD",
            departure_datetime=datetime(2024, 9, 12, 12, 0),
            arrival_datetime=datetime(
                2024, 9, 13, 2, 0
            ),  # 14 hours total duration for this leg
        ),
        FlightEvent(
            flight_number="XX2345",
            departure_city="MAD",
            arrival_city="PMI",
            departure_datetime=datetime(
                2024, 9, 13, 16, 0
            ),  # 4-hour wait time, total journey > 24 hours
            arrival_datetime=datetime(
                2024, 9, 14, 1, 0
            ),  # Ends after more than 24 hours from start
        ),
    ]
    return MockFlightEventProvider(flight_events)


# Override dependency with the mock provider for general tests
@pytest.fixture(autouse=True)
def override_journey_search_service(mock_provider):
    app.dependency_overrides[get_journey_search_service] = lambda: JourneySearchService(
        mock_provider
    )
    yield
    app.dependency_overrides = {}


# Fixture for the test client
@pytest.fixture
def client():
    return TestClient(app)
