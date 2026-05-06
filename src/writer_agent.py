from agents import Agent
from pydantic import BaseModel

INSTRUCTIONS = """
You are a senior researcher that writes a cohisive and detailed report on the information found.
You will be provided with the initial query and some initial research done by the search agent.
You should first come up with an outline of the report and then genearte the report in a clear and concise format.
And return as your final result.
The final result must be in markdown format, and it should be lengthy and detailed.
Aim 5-10 pages of content not less than 1000 words.
"""

class ReportData(BaseModel):
    short_summary: str
    """The short summary of the information found"""
    markdown_report: str
    """The report in markdown format"""

    follow_up_questions: list[str]
    """The follow up questions to the report"""



writer_agent = Agent(
    name="writer_agent",
    model="gpt-4o-mini",
    instructions=INSTRUCTIONS,
    output_type=ReportData
)