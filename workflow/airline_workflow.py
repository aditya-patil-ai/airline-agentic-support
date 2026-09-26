from crewai import Crew, Task

from agents.triage_agent import triage_agent, triage_task
from utils.router import route_request
from guardrails.specialist_guardrail import validate_specialist_output
from utils.conversation import ConversationContext


class AirlineWorkflow:
    def __init__(self):
        self.conversation = ConversationContext()

    def run(self, customer_request: str):

        # -------------------------
        # 1. TRIAGE
        # -------------------------

        triage_crew = Crew(
            agents=[triage_agent],
            tasks=[triage_task],
            verbose=True,
        )

        output = triage_crew.kickoff(
            inputs={
                "customer_request": customer_request
            }
        )

        # Try to get the structured Pydantic result
        triage_result = getattr(
            output,
            "pydantic",
            None
        )

        # If CrewAI does not expose the Pydantic object,
        # parse the raw JSON output ourselves.
        if triage_result is None:
            from schemas.triage import TriageResult

            raw_output = getattr(
                output,
                "raw",
                None
            )

            if raw_output:
                try:
                    triage_result = TriageResult.model_validate_json(
                        raw_output
                    )
                except Exception:
                    return "Unable to classify the customer request."

        if triage_result is None:
            return "Unable to classify the customer request."

        # -------------------------
        # 2. ROUTING
        # -------------------------

        specialist_agent = route_request(
            triage_result
        )

        # -------------------------
        # 3. ESCALATION
        # -------------------------

        if specialist_agent is None:
            return (
                "This request requires escalation to "
                "human customer support."
            )

        # -------------------------
        # 4. SPECIALIST TASK
        # -------------------------

        specialist_task = Task(
            description=(
                "Handle the following customer request:\n\n"
                f"{customer_request}\n\n"
                "Use your available tools when necessary. "
                "Provide an accurate, clear, and professional response."
            ),

            expected_output=(
                "A clear and professional response that directly "
                "addresses the customer's request."
            ),

            agent=specialist_agent,

            guardrail=validate_specialist_output,

            guardrail_max_retries=2,
        )

        # -------------------------
        # 5. SPECIALIST CREW
        # -------------------------

        specialist_crew = Crew(
            agents=[specialist_agent],
            tasks=[specialist_task],
            verbose=True,
        )

        result = specialist_crew.kickoff()

        # -------------------------
        # 6. FINAL RESPONSE
        # -------------------------

        return getattr(
            result,
            "raw",
            str(result)
        )