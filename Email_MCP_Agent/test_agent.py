from google.adk import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.genai import types
from agent import email_agent
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print("Testing the email_agent via MCP using Runner...")
    
    runner = Runner(
        app_name="test",
        agent=email_agent,
        session_service=InMemorySessionService(),
        auto_create_session=True
    )
    
    new_msg = types.Content(role="user", parts=[types.Part.from_text(text="Send a short test email to test@example.com with the subject 'MCP Test' and body 'Hello from the ADK email agent!'. Tell me if it succeeded.")])
    
    for event in runner.run(
        user_id="user1",
        session_id="session1",
        new_message=new_msg
    ):
        print("\n--- Event ---")
        print(event)

