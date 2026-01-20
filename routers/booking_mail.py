from fastapi import APIRouter

from schemas import form_request
from services.send_mail import send_mail

booking_mail_router = APIRouter()


@booking_mail_router.post("/")
async def send_booking_mail(
    booking_details: form_request.BookingRequest
) -> dict:
    """Send a booking email to admin.

    Args:
        booking_details (dict): Contains - N
        ame, email, booking date, and Message of the sender
    """
    booked_date = (
        booking_details.booked_date.strftime("%B %d, %Y") if \
            booking_details.booked_date else "Not provided"
    )
    
    phone = booking_details.phone or "Not provided"
    service = booking_details.service or "Not specified"
    content = booking_details.content or "No additional message"

    booking_section = f"""
        <h3>Booking Details</h3>
        <ul>
            <li><strong>Service:</strong> {service}</li>
            <li><strong>Requested Date:</strong> {booked_date}</li>
        </ul>

        <h3>Message</h3>
        <p>{content}</p>
    """ if booking_details.form_type.lower() == "booking" else f"""
        <h3>Message</h3>
        <p>{content}</p>
    """
    
    html_body = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>New Message Received</title>
            </head>
            <body style="font-family: Arial, sans-serif;">
                <h2 style="color:#c2a74e">Hi Legit Ink Team</h2>

                <p>You recevied a new request. Below are the details:</p>
                <h3>Client Details</h3>
                <ul>
                    <li><strong>Name:</strong> {booking_details.name}</li>
                    <li><strong>Email:</strong> {booking_details.email}</li>
                    <li><strong>Phone:</strong> {phone}</li>
                </ul>

                {booking_section}

                <br />

                <small>
                    This booking was submitted from the Legit Ink Tattoo website.
                </small>
            </body>
        </html>
    """

    return await send_mail(html_body, booking_details.form_type, "legitinktattoo@gmail.com")
 

@booking_mail_router.post("/response-mail")
async def send_response_mail(
    mail_details: form_request.BookingRequest
) -> dict:
    """Send a response email to the user who made the booking.
    Args:
        mail_details (dict): Contains
        form_type, name,  email, phone, booking date, and Message of the sender
    """
    booked_date = (
        mail_details.booked_date.strftime("%B %d, %Y") if \
            mail_details.booked_date else "Not provided"
    )
    
    phone = mail_details.phone or "Not provided"

    html_template = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Booking Confirmation</title>
    </head>
        <body style="font-family: Arial, sans-serif;">
            <h1>Legit Ink Received Your Booking 🎉!</h1>
            
            <p>Hello <strong>{mail_details.name}</strong></p>

            <p>
                We have received your booking request with the following details:
            </p>

            <ul>
                <li><strong>Service:</strong> {mail_details.service}</li>
                <li><strong>Appointment Date:</strong> {booked_date}</li>
                <li><strong>Phone:</strong> {phone}</li>
                <li><strong>Message:</strong> {mail_details.content}</li>
            </ul>
            <p>
                We look forward to your appointment! If any changes arise,
                we will notify you via email or chat.
            </p>

            <p>
                You can also chat with us on
                <a href="https://wa.me/2348140061166" target="_blank" rel="noopener">
                    WhatsApp
                </a>
            </p>

            <small>— Legit Ink Tattoo Team</small>
        </body>
    </html>
    """
    
    return await send_mail(html_template, mail_details.form_type, mail_details.email)
