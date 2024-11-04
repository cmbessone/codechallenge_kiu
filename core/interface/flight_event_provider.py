# core/interface/flight_event_provider.py
from abc import ABC, abstractmethod
from core.domain.models import FlightEvent
from typing import List


class FlightEventProvider(ABC):
    @abstractmethod
    def get_flight_events(self) -> List[FlightEvent]:
        """Abstract Method to obtain flight events"""
        pass
