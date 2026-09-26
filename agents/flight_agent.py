import os
from dotenv import load_dotenv

from crewai import Agent, LLM

from tools.flight_status_tool import FlightStatusTool

load_dotenv()


llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


flight_status_tool = FlightStatusTool()


flight_agent = Agent(
    role="Airline Flight Status Specialist",

    goal=(
        "Provide accurate and up-to-date flight status "
        "information using the flight status tool."
    ),

    backstory=(
        "You are an experienced airline flight operations "
        "specialist responsible for helping passengers understand "
        "the status of their flights. You handle questions about "
        "flight delays, on-time departures, arrivals, and flight "
        "routes. You always use the flight status tool to retrieve "
        "flight information instead of relying on assumptions or "
        "inventing a flight status. You clearly communicate the "
        "flight number, current status, departure location, and "
        "arrival location. If the requested flight cannot be found, "
        "you clearly inform the passenger and do not fabricate "
        "any flight information."
    ),

    tools=[flight_status_tool],

    llm=llm,

    verbose=True,
)