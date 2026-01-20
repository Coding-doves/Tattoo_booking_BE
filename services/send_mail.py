from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
import os

from schemas import form_request

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME = os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD"),
    MAIL_FROM = os.getenv("MAIL_FROM"),
    MAIL_PORT = int(os.getenv("MAIL_PORT")),
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME"),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    SUPPRESS_SEND = False # Set to True for testing without actually sending
)


async def send_mail(details: form_request.BookingRequest, content) -> dict:
    message = MessageSchema(
        subject=f"{details.form_type} by {details.name}",
        recipients=["legitinktattoo@gmail.com"],
        body=content,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    
    try:
        await fm.send_message(message)
        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"message": f"Error sending email: {str(e)}"}
