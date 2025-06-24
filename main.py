import os, sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if len(sys.argv) == 1:
    print('No message was entered, next time drop one in quotes like this: "Hey there".\nExiting now, bye.')
    sys.exit(1)
else:
    cl_contents = sys.argv[1]

response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents= cl_contents
)

print('\n',response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
