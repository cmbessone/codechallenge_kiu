from fastapi import APIRouter, HTTPException, Query, Depends
from datetime import datetime
from core.services.journey_search_service import JourneySearchService
from core.domain.models import Journey
from core.interface.flight_event_provider import FlightEventProvider
from infrastructure.in_memory_flight_event_provider import InMemoryFlightEventProvider

journey_router = APIRouter()


def get_flight_event_provider() -> FlightEventProvider:
    return InMemoryFlightEventProvider()


# Dependency for the JourneySearchService, allowing it to be overridden in tests
def get_journey_search_service(
    provider: FlightEventProvider = Depends(get_flight_event_provider),
) -> JourneySearchService:
    return JourneySearchService(provider)


@journey_router.get("/journeys/search", response_model=list[Journey])
async def search_journeys(
    date: str,
    from_: str = Query(..., alias="from"),
    to: str = Query(..., alias="to"),
    service: JourneySearchService = Depends(get_journey_search_service),
):
    try:
        search_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400, detail="Invalid date format. Use YYYY-MM-DD."
        )

    # Crear el servicio y buscar viajes
    journeys = service.find_journeys(search_date, from_, to)

    if not journeys:
        raise HTTPException(status_code=404, detail="No journeys found.")

    return journeys
