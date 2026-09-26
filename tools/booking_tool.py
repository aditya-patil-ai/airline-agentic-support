from crewai.tools import BaseTool

class BookingLookupTool(BaseTool):
    name : str = "booking_lookup_tool"

    description : str = (
        "Look up for passenger's booking using their confirmation number"
    )

    def _run(self, confirmation_number : str) -> str:
        bookings = {
            "ABC123" : {
                "passenger_name" : "John Cena",
                "flight_number" : "AIR201",
                "seat_number" : "5A",
                "destination" : "Bangalore",
                "status" : "confirmed"
            },
            "XYZ789": {
                "passenger_name": "Jane Smith",
                "flight_number": "AIR405",
                "seat_number": "10C",
                "destination": "Delhi",
                "status": "Confirmed",
            },
        }

        booking = bookings.get(confirmation_number.upper())

        if not booking:
            return (
                f"NO booking found for the confirmation number {confirmation_number}."
            )

        return (
            f"Passenger : {booking['passenger_name']}\n"
            f"Flight : {booking['flight_number']}\n"
            f"Seat : {booking['seat_number']}\n"
            f"Destination : {booking['destination']}\n"
            f"Status : {booking['status']}"
        )
    