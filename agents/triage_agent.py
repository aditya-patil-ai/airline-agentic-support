import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
from guardrails.triage_guardrail import validate_triage_output
from schemas.triage import TriageResult

llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)

triage_agent = Agent(
    role="Airline Customer Service Triage Specialist",

    goal=(
        "Analyze customer requests and determine "
        "which category they belong to."
    ),

    backstory=(
        "You are the first point of contact for airline "
        "customers. You carefully analyze their requests "
        "and classify them for the appropriate specialist."
    ),
    
    llm=llm,
    verbose=True,
)

triage_task = Task(
    description=(
        "Analyze the following customer request:\n\n"
        "{customer_request}\n\n"

        "Classify the request into exactly one of these categories:\n"
        "- faq\n"
        "- seat\n"
        "- booking\n"
        "- flight\n"
        "- baggage\n"
        "- cancellation\n"
        "- escalation\n\n"

        "Return the category, confidence score, "
        "and a short reason for your classification."
    ),

    expected_output=(
        "A structured TriageResult containing the category, "
        "confidence score between 0 and 1, and reason."
    ),

    output_pydantic=TriageResult,

    guardrail=validate_triage_output,

    guardrail_max_retries=2,

    agent=triage_agent,
)

