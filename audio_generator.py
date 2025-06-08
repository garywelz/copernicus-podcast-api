import os
import httpx
import uuid

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Default: Rachel (you can customize this later)

AUDIO_OUTPUT_DIR = "audio"
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

async def generate_audio(script_text: str, voice: str = "default") -> str:
    if voice != "default":
        VOICE_ID = voice  # Override if custom voice provided

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": script_text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    audio_path = os.path.join(AUDIO_OUTPUT_DIR, f"{uuid.uuid4()}.mp3")

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Audio generation failed: {response.text}")

        with open(audio_path, "wb") as f:
            f.write(response.content)

    return audio_path
