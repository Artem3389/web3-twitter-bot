
import os

print("🔍 ALL ENVIRONMENT VARIABLES:")
for key, value in os.environ.items():
    print(f"{key} = {value}")

API_TOKEN = os.getenv("7670472776:AAFKugaQ4aBEM3lN9ioQJbRrIT3JI6zaM")
print("🔍 DEBUG_API_TOKEN:", repr(API_TOKEN))

if not API_TOKEN:
    raise ValueError("API_TOKEN environment variable not set")
