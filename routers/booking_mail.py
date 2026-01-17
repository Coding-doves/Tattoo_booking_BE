from fastapi import APIRouter, HTTPException

booking_mail_router = APIRouter()

@booking_mail_router.post("/")
async def send_booking_mail(booking_details: dict) -> None:
    """Send a booking email.

    Args:
        booking_details (dict): Contains, Name, email, booking date, and Message of the sender
    """
    
    pass
