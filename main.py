import json
import re
import subprocess
import os
from dotenv import load_dotenv

import openai

from typing import List, Dict, Any

load_dotenv()

# OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key


def get_new_thoughts() -> List[Dict[str, str]]:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Generate 10 responses that represent thoughts of a girl who feels a lot of pressure from society to be perfect, and who is becoming crazy and doesn't understand the reality and what is going on.",  # noqa: E501
        },
        {
            "role": "user",
            "content": "Please generate the responses. Make sure there is no empty response.",  # noqa: E501
        },
    ]
    response: Any = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    responses: List[str] = response.choices[0].message["content"].split("\n")[:10]
    formatted_responses: List[Dict[str, str]] = [
        {"response": re.sub(r"^\d+\.\s*", "", resp).strip()} for resp in responses
    ]
    return formatted_responses


# Get new thoughts
new_data = get_new_thoughts()

# Write the new data to output.json (overwriting existing data)
with open("output.json", "w") as f:
    json.dump(new_data, f, indent=4)

# Add all changes to Git
subprocess.run(["git", "add", "output.json"])

# Commit changes with a message
subprocess.run(["git", "commit", "-m", "Update output.json"])

# Push changes to GitHub
subprocess.run(["git", "push"])
