import os
from models import PodcastRequest, PodcastResponse

# These will be filled in later
from ai_script_generator import generate_script_and_description
from audio_generator import generate_audio
from image_generator import generate_thumbnail
from uploader import upload_to_gcs

async def generate_podcast_assets(request: PodcastRequest) -> PodcastResponse:
    # 1. Generate script and description
    script, description, title = await generate_script_and_description(request.prompt, request.length)

    # 2. Generate audio
    audio_path = await generate_audio(script, request.voice)

    # 3. Generate thumbnail
    image_path = await generate_thumbnail(request.prompt)

    # 4. Upload both
    audio_url = await upload_to_gcs(audio_path, "audio")
    image_url = await upload_to_gcs(image_path, "images")

    # 5. Package result
    return PodcastResponse(
        title=title,
        description=description,
        audio_url=audio_url,
        image_url=image_url
    )
