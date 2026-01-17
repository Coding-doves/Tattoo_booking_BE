from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import instafeed

app = FastAPI()

# Allow vercel.app and localhost origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://legit-ink-tatoo.vercel.app/", "http://localhost:5000"],
    allow_methods=['GET', 'POST'],
    allow_headers=["*"],
)

app.include_router(instafeed.feed_router, prefix="/api/v1/instafeed", tags=["Instafeed"])


@app.get("/")
def main():
    return {'message': 'Legit Ink Tattoo API'}
