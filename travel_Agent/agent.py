from google.adk.agents import Agent
from google.adk.tools import google_search

travel_sub_agent = Agent(
    name="trip_planning_agent",
    model="gemini-2.5-flash",
    instruction="""You are a school trip planning expert. Your job is to help the school principal plan a school trip.""",
    description="You are a school trip planning expert.",
)

food_agent = Agent(
    name="food_agent",
    model="gemini-2.5-flash",
    instruction="""You are a school trip food expert. Your job is to help the school principal plan a school trip. Your response should be in the following format: - Improvements - Questions""",
    description="You are a school trip planning expert.",
)

hotel_agent = Agent(
    name="hotel_agent",
    model="gemini-2.5-flash",
    instruction="""You are a school trip hotel expert. Your job is to help the school principal plan a school trip. Your response should be in the following format: - Improvements - Questions""",
    description="You are a school trip planning expert.",
)

history_agent = Agent(
    name="history_agent",
    model="gemini-2.5-flash",
    instruction="""You are a school history teacher. You are planning a history trip for students. Your job is to make a history trip plan according to the school principal's instructions. Your response should be in the following format: - Improvements - Questions""",
    description="You are a school history teacher.",
)

root_agent = Agent(
    name="travel_agent",
    model="gemini-2.5-flash",
    sub_agents=[travel_sub_agent, food_agent, hotel_agent, history_agent],
    instruction="""You are a school principal.
Your job is to make a school field trip plan.

Your response should be in the following format:
- Itinerary
- Budget
- Questions

When you are done, reply with "DONE".""",
)
