from pydantic import BaseModel

class PodcastRequest(BaseModel):
    prompt: str
    voice: str = "default"
    length: str = "3min"

class PodcastResponse(BaseModel):
    title: str
    description: str
    audio_url: str
    image_url: str
