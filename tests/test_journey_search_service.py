from datetime import datetime
from core.services.journey_search_service import JourneySearchService


def test_find_direct_journey(mock_provider):
    service = JourneySearchService(mock_provider)
    journeys = service.find_journeys(datetime(2024, 9, 12), "BUE", "MAD")

    assert len(journeys) == 1
    assert journeys[0].connections == 1
    assert journeys[0].path[0].flight_number == "XX1234"


def test_find_journey_with_connection(mock_provider):
    service = JourneySearchService(mock_provider)
    journeys = service.find_journeys(datetime(2024, 9, 12), "BUE", "PMI")

    assert len(journeys) == 1
    assert journeys[0].connections == 2
    assert journeys[0].path[0].flight_number == "XX1234"
    assert journeys[0].path[1].flight_number == "XX2345"
