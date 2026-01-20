"""from dotenv import load_dotenv
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr
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
    MAIL_STARTTLS = False88,
    MAIL_SSL_TLS = True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True,
    SUPPRESS_SEND = False # Set to True for testing without actually sending
)


async def send_mail(
    content, email: EmailStr = "legitinktattoo@gmail.com"
) -> dict:
    message = MessageSchema(
        subject=f"New Message",
        recipients=[email],
        body=content,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    
    try:
        await fm.send_message(message)
        return {"message": "Email sent successfully!"}
    except Exception as e:
        return {"message": f"Error sending email: {str(e)}"}
"""

from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi.concurrency import run_in_threadpool
import os
from pydantic import EmailStr
import smtplib

load_dotenv()

def _send_mail_sync(content: str, email: EmailStr):
    sender_email = os.getenv("MAIL_USERNAME")
    password = os.getenv("MAIL_PASSWORD")

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = "New Message"

    message.attach(MIMEText(content, "html", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)


async def send_mail(content: str, email: EmailStr = "legitinktattoo@gmail.com") -> str:
    await run_in_threadpool(_send_mail_sync, content, email)
    return "Email sent successfully!"
