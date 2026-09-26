import os
from dotenv import load_dotenv

from crewai import Agent, LLM

from tools.baggage_tool import BaggageTool

load_dotenv()


llm = LLM(
    model="groq/openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
)


baggage_tool = BaggageTool()


baggage_agent = Agent(
    role="Airline Baggage Specialist",

    goal=(
        "Help passengers understand their baggage allowance "
        "and baggage-related policies."
    ),

    backstory=(
        "You are an experienced airline baggage specialist "
        "responsible for helping passengers understand baggage "
        "allowances and related policies. You handle questions "
        "about carry-on and checked baggage, including permitted "
        "weight, dimensions, and applicable restrictions. You "
        "always use the baggage tool to retrieve the available "
        "baggage information instead of making assumptions or "
        "inventing airline policies. You provide clear and "
        "professional answers and explain the information in a "
        "simple way that passengers can easily understand. If "
        "the requested baggage information is unavailable, you "
        "clearly communicate that instead of guessing."
    ),

    tools=[baggage_tool],

    llm=llm,

    verbose=True,
)