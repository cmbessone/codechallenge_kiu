from datetime import datetime
from pydantic import BaseModel


class FlightEvent(BaseModel):
    flight_number: str
    departure_city: str
    arrival_city: str
    departure_datetime: datetime
    arrival_datetime: datetime

    @property
    def event_id(self):
        return f"{self.flight_number}_{self.departure_datetime.strftime('%Y%m%d')}"


class Journey(BaseModel):
    connections: int
    path: list[FlightEvent]
