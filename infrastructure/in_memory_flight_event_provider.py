from core.interface.flight_event_provider import FlightEventProvider
from core.domain.models import FlightEvent
from datetime import datetime
from typing import List


class InMemoryFlightEventProvider(FlightEventProvider):
    def get_flight_events(self) -> List[FlightEvent]:
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
