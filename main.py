from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from models import PodcastRequest, PodcastResponse
from podcast_generator import generate_podcast_assets

load_dotenv()
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Copernicus Podcast API is live"}

@app.post("/generate-podcast", response_model=PodcastResponse)
async def generate_podcast(request: PodcastRequest):
    try:
        result = await generate_podcast_assets(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
