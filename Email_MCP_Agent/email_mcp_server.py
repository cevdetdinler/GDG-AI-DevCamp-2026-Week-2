import os
import smtplib
from email.message import EmailMessage
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("email_server")

@mcp.tool()
def send_email(to_email: str, subject: str, body: str) -> str:
    """Send an email using SMTP.
    
    Args:
        to_email: The recipient's email address.
        subject: The subject of the email.
        body: The content of the email.
    """
    sender_email = os.environ.get("SMTP_EMAIL")
    sender_password = os.environ.get("SMTP_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))

    if not sender_email or not sender_password:
        return "Error: SMTP_EMAIL or SMTP_PASSWORD environment variables are not set."

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return f"Successfully sent email to {to_email}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == "__main__":
    # When run directly, start the stdio MCP server
    mcp.run()
    while mcp.running:
        pass
    else:
        mcp.stop()
