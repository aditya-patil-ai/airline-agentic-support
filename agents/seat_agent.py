import os
from dotenv import load_dotenv

from crewai import Agent, LLM

from tools.seat_tool import SeatUpdateTool

load_dotenv()


llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


seat_tool = SeatUpdateTool()


seat_agent = Agent(
    role = "Airline Seat Booking Specialist",

    goal = (
        "Help passengers update their flight seat accurately "
        "using their confirmation number and desired seat."
    ),

    backstory=(
        "You are an experienced airline seat booking specialist "
        "responsible for helping passengers manage their seat "
        "assignments. You carefully collect the passenger's "
        "confirmation number and desired seat number before "
        "performing any seat change. You use the seat update tool "
        "to perform the operation rather than claiming that a "
        "change was completed without using the tool. You provide "
        "clear and professional responses and never invent booking "
        "details. If the request is unrelated to seat management, "
        "the request should be handled by the appropriate specialist."
    ),

    tools = [seat_tool],

    llm = llm,

    verbose = True,
)