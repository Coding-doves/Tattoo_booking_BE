from fastapi import APIRouter, HTTPException
from schemas import form_request

booking_mail_router = APIRouter()


@booking_mail_router.post("/")
async def send_booking_mail(booking_details: form_request.BookingRequest) -> dict:
    """Send a booking email.

    Args:
        booking_details (dict): Contains, Name, email, booking date, and Message of the sender
    """
    
    print(booking_details.model_dump())
    
    return {"message": "Booking received yeah!"}
