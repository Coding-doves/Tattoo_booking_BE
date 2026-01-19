from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

class BookingRequest(BaseModel):
    name: str
    email: EmailStr
    booked_date: Optional[date] = None
    phone: Optional[str] = None
    app_goal: Optional[str] = None
    desription: str
