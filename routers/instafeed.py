from fastapi import APIRouter, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
feed_router = APIRouter()

INSTAFEED_TOKEN = os.getenv("INSTAGRAM_TOKEN")

@feed_router.get("/")
async def get_instafeed():
    if not INSTAFEED_TOKEN:
        raise HTTPException(status_code=500, detail="Instagram token not configured")
    
    url = (
        "https://graph.instagram.com/me/media"
        "?fields=id,caption,media_url,permalink,media_type"
        f"&access_token={INSTAFEED_TOKEN}"
    )
    
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url)
        
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch Instagram feed")
    
    return response.json()
