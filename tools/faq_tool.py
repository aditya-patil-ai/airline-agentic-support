from crewai.tools import BaseTool


class FAQTool(BaseTool):
    name: str = "faq_lookup_tool"

    description: str = (
        "Lookup frequently asked questions about the airline, "
        "including baggage, seating, and WiFi."
    )

    def _run(self, question: str) -> str:
        question_lower = question.lower()

        if any(
            keyword in question_lower
            for keyword in [
                "bag",
                "baggage",
                "luggage",
                "carry-on",
                "hand luggage",
                "hand carry",
            ]
        ):
            return (
                "You are allowed to bring one bag on the plane. "
                "It must be under 50 pounds and "
                "22 inches x 14 inches x 9 inches."
            )

        elif any(
            keyword in question_lower
            for keyword in [
                "seat",
                "seats",
                "seating",
                "plane",
            ]
        ):
            return (
                "There are 120 seats on the plane. "
                "There are 22 business class seats and "
                "98 economy seats. "
                "Exit rows are rows 4 and 16. "
                "Rows 5-8 are Economy Plus, "
                "with extra legroom."
            )

        elif any(
            keyword in question_lower
            for keyword in [
                "wifi",
                "internet",
                "wireless",
                "connectivity",
                "network",
                "online",
            ]
        ):
            return (
                "We have free WiFi on the plane. "
                "Join Airline-Wifi."
            )

        return "I'm sorry, I don't know the answer to that question."

