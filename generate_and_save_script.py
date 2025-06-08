from openai import OpenAI
from secrets_loader import get_secret
import os

# Set up OpenAI client with key from Google Secret Manager
client = OpenAI(api_key=get_secret("openai-api-key"))

# Prompt to generate a script
prompt = "Write a 2-minute podcast script about the latest developments in neuroscience."

# Request completion from OpenAI
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a podcast script writer."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
)

# Extract the message content
script_text = response.choices[0].message.content.strip()

# Create the output directory if needed
os.makedirs("output", exist_ok=True)

# Save to file
with open("output/script.txt", "w", encoding="utf-8") as f:
    f.write(script_text)

print("✅ Script saved to output/script.txt")
