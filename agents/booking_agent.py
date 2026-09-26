import os
from dotenv import load_dotenv

from crewai import Agent, LLM

from tools.booking_tool import BookingLookupTool

load_dotenv()


llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    additional_params={
        "drop_params": True
    },
)


booking_tool = BookingLookupTool()


booking_agent = Agent(
    role="Airline Booking Specialist",

    goal=(
        "Help passengers retrieve and understand their booking "
        "information using their confirmation number."
    ),

    backstory=(
        "You are an experienced airline booking specialist "
        "responsible for helping passengers retrieve accurate "
        "booking information. You handle requests involving "
        "passenger details, flight numbers, seat assignments, "
        "destinations, and booking status. You always ask for or "
        "use the passenger's confirmation number when a booking "
        "lookup is required. You rely on the booking lookup tool "
        "to retrieve information rather than guessing or inventing "
        "booking details. You communicate the retrieved information "
        "clearly and professionally. If no booking is found, you "
        "inform the passenger clearly instead of making assumptions."
    ),

    tools=[booking_tool],

    llm=llm,

    verbose=True,
)