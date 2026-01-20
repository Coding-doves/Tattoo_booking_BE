from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi.concurrency import run_in_threadpool
import os
from pydantic import EmailStr
import smtplib
import traceback

load_dotenv()


def _send_mail_sync(content: str, form_type, email: EmailStr):
    sender_email = os.getenv("MAIL_USERNAME")
    password = os.getenv("MAIL_PASSWORD")

    if not sender_email or not password:
        raise RuntimeError("MAIL_USERNAME or MAIL_PASSWORD not set")

    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = f"{form_type} from Legit Ink Tattoo"
    message.attach(MIMEText(content, "html", "utf-8"))

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)


async def send_mail(content: str, form_type: str, email: EmailStr) -> dict:
    try:
        await run_in_threadpool(_send_mail_sync, content, form_type, email)
        return {"message": "Email sent successfully"}
    except Exception as e:
        traceback.print_exc()  # 👈 CRITICAL
        raise e
    