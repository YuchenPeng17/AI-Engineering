import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(dotenv_path="../.env")
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-5-nano-2025-08-07",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write hello world with many exclamation points"
        }
    ]
)
 
print(completion.choices[0].message)