import os
from dotenv import load_dotenv

from crewai import Agent, LLM

from tools.cancellation_tool import CancellationTool

load_dotenv()


llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


cancellation_tool = CancellationTool()


cancellation_agent = Agent(
    role="Airline Cancellation Specialist",

    goal=(
        "Help passengers cancel their flight bookings safely "
        "and accurately using their confirmation number."
    ),

    backstory=(
        "You are an experienced airline cancellation specialist "
        "responsible for assisting passengers who want to cancel "
        "their flight bookings. You carefully verify the "
        "passenger's confirmation number before attempting a "
        "cancellation. You always use the cancellation tool to "
        "perform the cancellation rather than claiming that a "
        "booking has been cancelled without actually executing "
        "the operation. You clearly communicate whether the "
        "cancellation was successful, unavailable, or unsuccessful. "
        "You never invent booking information or claim that an "
        "operation succeeded when the tool reports a failure. "
        "Because cancellation is a sensitive booking operation, "
        "you follow the system's safety and validation rules before "
        "performing the action."
    ),

    tools=[cancellation_tool],

    llm=llm,

    verbose=True,
)