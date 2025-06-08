from secrets_loader import get_secret

print("Loaded secret value:")
print(get_secret("openai-api-key"))
