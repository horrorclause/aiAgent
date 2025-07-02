import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import type

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) == 1:
    print('No message was entered, next time drop one in quotes like this: "Hey there".\nExiting now, bye.')
    sys.exit(1)
else:
    user_prompt = sys.argv[1]

messages = [
    types.Content(role="user",parts=[types.Part(text=user_prompt)])
]

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents= messages,
)

print('\n',response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
