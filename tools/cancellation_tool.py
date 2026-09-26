from crewai.tools import BaseTool


class CancellationTool(BaseTool):
    name: str = "cancellation_tool"

    description: str = (
        "Cancel a passenger's flight booking using their "
        "confirmation number."
    )

    def _run(self, confirmation_number: str) -> str:

        cancellable_bookings = {
            "ABC123": True,
            "XYZ789": False,
        }

        can_cancel = cancellable_bookings.get(
            confirmation_number.upper()
        )

        if can_cancel is None:
            return (
                f"No booking found for confirmation "
                f"number {confirmation_number}."
            )

        if not can_cancel:
            return (
                f"Booking {confirmation_number.upper()} "
                "cannot be cancelled at this time."
            )

        return (
            f"Booking {confirmation_number.upper()} "
            "has been successfully cancelled."
        )