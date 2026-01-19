from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class BookingRequest(BaseModel):
    form_type: str
    name: str
    email: EmailStr
    date: Optional[datetime] = None
    phone: Optional[str] = None
    service: Optional[str] = None
    content: str
