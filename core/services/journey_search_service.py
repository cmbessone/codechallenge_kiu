from datetime import timedelta, datetime
from core.domain.models import Journey
from core.interface.flight_event_provider import FlightEventProvider
import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class JourneySearchService:
    MAX_TOTAL_DURATION = timedelta(hours=24)  # Maximum allowed journey duration
    MAX_LAYOVER_TIME = timedelta(
        hours=4
    )  # Maximum allowed layover time between connections

    def __init__(self, provider: FlightEventProvider):
        self.provider = provider

    def find_journeys(
        self, date: datetime, origin: str, destination: str
    ) -> list[Journey]:
        # Retrieve events from provider
        flight_events = self.provider.get_flight_events()

        # Define the search window for the selected date and the following day
        start_of_day = datetime(date.year, date.month, date.day)
        end_of_next_day = start_of_day + timedelta(days=2)

        logger.debug(
            "Searching for journeys from %s to %s on %s",
            origin,
            destination,
            date.strftime("%Y-%m-%d"),
        )

        # Filter flights within the extended date range
        flights_in_range = [
            event
            for event in flight_events
            if start_of_day <= event.departure_datetime < end_of_next_day
        ]

        logger.debug(
            "Flights in range: %s",
            [
                f"{event.departure_city}-{event.arrival_city} ({event.departure_datetime})"
                for event in flights_in_range
            ],
        )

        journeys = []

        for event in flights_in_range:
            # Direct flight case
            if event.departure_city == origin and event.arrival_city == destination:
                logger.debug("Direct flight found: %s to %s", origin, destination)
                journeys.append(Journey(connections=1, path=[event]))
            # Check for connecting flights
            elif event.departure_city == origin:
                for connection in flights_in_range:
                    if (
                        connection.departure_city == event.arrival_city
                        and connection.arrival_city == destination
                    ):
                        time_between = (
                            connection.departure_datetime - event.arrival_datetime
                        )
                        total_duration = (
                            connection.arrival_datetime - event.departure_datetime
                        )

                        logger.debug(
                            "Checking connection from %s to %s via %s. Time between: %s, Total duration: %s",
                            origin,
                            destination,
                            event.arrival_city,
                            time_between,
                            total_duration,
                        )

                        # Verify connection and total journey constraints
                        if (
                            time_between <= self.MAX_LAYOVER_TIME
                            and total_duration <= self.MAX_TOTAL_DURATION
                        ):
                            logger.debug(
                                "Valid connection found via %s", event.arrival_city
                            )
                            journeys.append(
                                Journey(connections=2, path=[event, connection])
                            )
                        else:
                            logger.debug(
                                "Invalid connection via %s (Time between: %s, Total duration: %s)",
                                event.arrival_city,
                                time_between,
                                total_duration,
                            )

        if not journeys:
            logger.debug(
                "No journeys found from %s to %s on %s",
                origin,
                destination,
                date.strftime("%Y-%m-%d"),
            )

        return journeys
