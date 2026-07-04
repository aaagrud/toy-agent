import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if not api_key:
    raise RuntimeError("Please add api key in .env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

messages=[
    {
        "role": "user",
        "content": args.user_prompt
    },
]
response = client.chat.completions.create(
    model = "openrouter/free",
    messages = messages
)
if not response.usage:
    raise RuntimeError("Failed API Request")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Response tokens: {response.usage.completion_tokens}")
print(f"Response: {response.choices[0].message.content}")
