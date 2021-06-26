import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SEND_GRID_API = os.getenv("SEND_GRID_API")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS")

print(SEND_GRID_API)
print(SENDER_ADDRESS)

print(type(SEND_GRID_API))
print(type(SENDER_ADDRESS))