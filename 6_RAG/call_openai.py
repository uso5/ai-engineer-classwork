import pandas as pd
import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def create_prompt(search_results, user_question):
    context = "\n\n".join(search_results)
    prompt = f"Context: {context}\nQuestion: {user_question}\nAnswer:"
    return prompt


def query_openai_chat(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response
