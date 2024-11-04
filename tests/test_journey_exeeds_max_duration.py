# tests/test_journey_exeeds_max_duration.py

from datetime import datetime
from core.services.journey_search_service import JourneySearchService


def test_journey_exceeds_max_duration(mock_provider_exceeding_max_duration):
    # Test that journeys exceeding the max duration are correctly excluded

    service = JourneySearchService(mock_provider_exceeding_max_duration)
    journeys = service.find_journeys(datetime(2024, 9, 12), "BUE", "PMI")

    assert len(journeys) == 0  # Expecting no valid journeys due to duration constraints
