from openai import OpenAI
from secrets_loader import get_secret

client = OpenAI(api_key=get_secret("openai-api-key"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{
        "role": "user",
        "content": "Summarize the latest news in neuroscience in under 60 seconds."
    }]
)

print(response.choices[0].message.content)
