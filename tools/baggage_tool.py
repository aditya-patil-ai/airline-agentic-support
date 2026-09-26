from crewai.tools import BaseTool


class BaggageTool(BaseTool):
    name: str = "baggage_tool"

    description: str = (
        "Provide information about airline baggage allowances "
        "and baggage fees."
    )

    def _run(self, baggage_type: str) -> str:

        baggage_info = {
            "carry-on": (
                "1 carry-on bag is allowed. "
                "Maximum weight: 50 pounds. "
                "Maximum dimensions: 22 x 14 x 9 inches."
            ),
            "checked": (
                "1 checked bag is allowed. "
                "Maximum weight: 50 pounds. "
                "Additional checked bags may require a fee."
            ),
        }

        baggage = baggage_info.get(baggage_type.lower())

        if not baggage:
            return (
                "Please specify either 'carry-on' "
                "or 'checked' baggage."
            )

        return baggage