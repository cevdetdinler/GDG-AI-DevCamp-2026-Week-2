import os
import sys
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from mcp import StdioServerParameters


email_mcp_toolset = McpToolset(
    connection_params=StdioServerParameters(
        command=sys.executable,
        args=[os.path.join(os.path.dirname(__file__), "email_mcp_server.py")]
    )
)

email_agent = Agent(
    name="email_agent",
    model="gemini-2.5-flash",
    instruction="""You are an email communication expert. 
Your job is to send emails using your tools when requested. 
Draft and send emails containing the travel plans or other requested information to the specified recipients.""",
    description="You are an email communication expert.",
    tools=[email_mcp_toolset]
)

