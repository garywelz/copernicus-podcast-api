import os
import base64
from openai import OpenAI
from secrets_loader import get_secret

# Load OpenAI API key from Secret Manager
client = OpenAI(api_key=get_secret("openai-api-key"))

# Define the image generation prompt
prompt = (
    "A stylized podcast thumbnail about cutting-edge neuroscience, featuring a mind-controlled robotic arm, "
    "glowing brain with memory visuals, and light beams representing optogenetics. Futuristic, clean, modern style "
    "with deep blue and purple tones. Square format, 640x640 pixels."
)

# Generate the image
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard",
    n=1
)

# Get the URL of the image
image_url = response.data[0].url

# Download and save the image
import requests

os.makedirs("output", exist_ok=True)
image_path = "output/thumbnail.png"
with open(image_path, "wb") as f:
    f.write(requests.get(image_url).content)

print(f"Thumbnail saved to: {image_path}")
