from crewai.tools import BaseTool


class SeatUpdateTool(BaseTool):
    name: str = "update_seat_tool"

    description: str = (
        "Update a passenger's seat using their "
        "confirmation number and desired seat number."
    )

    def _run(self, confirmation_number: str, new_seat: str) -> str:

        return (
            f"Updated seat to {new_seat} "
            f"for confirmation number {confirmation_number}."
        )