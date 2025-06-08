import requests
import os
from secrets_loader import get_secret

# Load script text
with open("output/script.txt", "r", encoding="utf-8") as f:
    script = f.read()

# ElevenLabs API setup
api_key = get_secret("elevenlabs-api-key")  # You’ll need to upload this to Secret Manager
voice_id = "EXAVITQu4vr4xnSDxMaL"  # Default voice ID (e.g., Rachel)

url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

payload = {
    "text": script,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.75
    }
}

# Send request
response = requests.post(url, headers=headers, json=payload)

# Save the audio
os.makedirs("output", exist_ok=True)
with open("output/script.wav", "wb") as f:
    f.write(response.content)

print("✅ Audio saved to output/script.wav")
