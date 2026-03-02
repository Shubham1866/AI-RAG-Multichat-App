import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

CHAT_MODEL = "gpt-4o-mini"


def generate_answer(messages: list[dict]) -> str:
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=messages,
        temperature=0.2
    )
    return response.choices[0].message.content