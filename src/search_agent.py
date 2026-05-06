from agents import Agent, WebSearchTool, ModelSettings

INSTRUCTIONS = """
You are a search agent that searches the web for the best information.
You will be given a search term to search the web for.
And produce a concise summary of the information found.
The summary must have 2-3 paragraphs of information and less than 300 words.
Capture the key points and insights from the information found.
The summary must be in a clear and concise format.
The summary must be in a language that is easy to understand.
The summary must be in a language that is easy to understand.
Do not include any other information in the summary.
"""

search_agent = Agent(
    name="search_agent",
    model="gpt-4o-mini",
    instructions=INSTRUCTIONS,
    tools=[WebSearchTool(search_context_size="low")],
    model_settings=ModelSettings(tool_choice="required")
)