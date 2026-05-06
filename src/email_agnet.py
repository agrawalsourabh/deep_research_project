import os

from agents import Agent, function_tool


INSTRUCTIONS = """
You are a email agent that sends an email.
You will be given a email address, subject and body.
You will need to send an email to the given email address.
You will need to return a message indicating the email was sent successfully.
Provided the report is converted in to clean html format, use the html format to send the email.
And use the following email address to send the email:

"""

@function_tool
def send_email(email: str, subject: str, body: str) -> str:
    """Send an email to the given email address"""
    return f"Email sent to {email} with subject {subject} and body {body}"

email_agent = Agent(
    name="email_agent",
    model="gpt-4o-mini",
    tools=[send_email],
    instructions=INSTRUCTIONS
)