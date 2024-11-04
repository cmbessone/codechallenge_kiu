from datetime import datetime
from core.domain.models import FlightEvent


def test_event_id_generation():
    # Create a sample FlightEvent instance
    flight_event = FlightEvent(
        flight_number="XX1234",
        departure_city="BUE",
        arrival_city="MAD",
        departure_datetime=datetime(2024, 9, 12, 12, 0),
        arrival_datetime=datetime(2024, 9, 13, 0, 0),
    )

    # Assert that the event_id is generated correctly
    expected_event_id = "XX1234_20240912"
    assert (
        flight_event.event_id == expected_event_id
    ), f"Expected {expected_event_id}, but got {flight_event.event_id}"
