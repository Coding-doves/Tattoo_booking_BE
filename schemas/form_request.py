from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class BookingRequest(BaseModel):
    form_type: str
    name: str
    email: EmailStr
    booked_date: Optional[date] = None
    phone: Optional[str] = None
    service: Optional[str] = None
    content: Optional[str] = None
