from crewai.tools import BaseTool


class FlightStatusTool(BaseTool):
    name: str = "flight_status_tool"

    description: str = (
        "Check the current status of an airline flight "
        "using its flight number."
    )

    def _run(self, flight_number: str) -> str:

        flights = {
            "AI202": {
                "status": "On Time",
                "departure": "Bengaluru",
                "arrival": "Mumbai",
            },
            "AI405": {
                "status": "Delayed",
                "departure": "Bengaluru",
                "arrival": "Delhi",
            },
        }

        flight = flights.get(flight_number.upper())

        if not flight:
            return (
                f"No flight found for flight number "
                f"{flight_number}."
            )

        return (
            f"Flight: {flight_number.upper()}\n"
            f"Status: {flight['status']}\n"
            f"Departure: {flight['departure']}\n"
            f"Arrival: {flight['arrival']}"
        )