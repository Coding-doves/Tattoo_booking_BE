from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import instafeed, booking_mail

app = FastAPI()

# Allow vercel.app and localhost origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://legit-ink-tatoo.vercel.app/", "http://localhost:5000"],
    allow_methods=['GET', 'POST'],
    allow_headers=["*"],
)

app.include_router(instafeed.feed_router, prefix="/api/v1/instafeed", tags=["Instafeed"])
app.include_router(booking_mail.booking_mail_router, prefix="api/v1/send-booking-mail", tags=["Booking Mail"])


@app.get("/")
def main():
    return {'message': 'Legit Ink Tattoo API'}
