from typing import Any

from pydantic import BaseModel
from agents import Agent

TOTAL_SEARCHES = 2

INSTRUCTIONS = """
You are a planner agent that plans the best research to perform.
You will be given a message from the user.
You will need to plan the best research to perform.
You will need to return a list of searches to perform the best research.
You will need to return a list of {TOTAL_SEARCHES} searches.
"""



class WebSearchItem(BaseModel):
    reason: str
    """Your reasoning why this is important for the query"""
    
    query: str
    """The query to search the web for"""


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """The list of searches to perform the best research"""


planner_agent = Agent(
    name="planner_agent",
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
    instructions=INSTRUCTIONS.format(TOTAL_SEARCHES=TOTAL_SEARCHES)
)