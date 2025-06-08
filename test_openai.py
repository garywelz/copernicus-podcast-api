from openai import OpenAI
from secrets_loader import get_secret

# Load the secret key from Google Secret Manager
api_key = get_secret("openai-api-key")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Send a simple message to test the API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)

# Print the reply
print(response.choices[0].message.content)