# ai_script_generator.py

from secrets_loader import get_secret
from openai import OpenAI
import google.generativeai as genai

# Fetch secrets from Google Secret Manager
openai_api_key = get_secret("openai-api-key")
gemini_api_key = get_secret("gemini-api-key")

# Initialize API clients
client = OpenAI(api_key=openai_api_key)
genai.configure(api_key=gemini_api_key)

def generate_script_and_description(prompt: str) -> dict:
    """
    Generates a podcast script and description from a prompt using GPT-4.
    Falls back to Gemini if GPT-4 fails.
    """
    try:
        print("[Using GPT-4]")
        chat = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a science podcast scriptwriter."},
                {"role": "user", "content": prompt}
            ]
        )
        response = chat.choices[0].message.content
    except Exception as e:
        print("[GPT-4 failed] Falling back to Gemini:\n", e)
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(prompt).text

    # Split response into script and description
    parts = response.split("DESCRIPTION:")
    script = parts[0].strip()
    description = parts[1].strip() if len(parts) > 1 else ""
    return {"script": script, "description": description}
