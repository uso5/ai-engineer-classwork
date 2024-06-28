import pandas as pd
import numpy as np
from openai import OpenAI
import tiktoken 
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def prepare_tweet_data(filepath, token_limit=2048):
    # Read the entire file
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    # Initialize the tokenizer with the correct encoding
    tokenizer = tiktoken.get_encoding("cl100k_base")

    # Tokenize the entire content
    tokens = tokenizer.encode(content)
    
    # Split tokens into chunks within the token limit
    chunks = []
    for i in range(0, len(tokens), token_limit):
        chunk_tokens = tokens[i:i + token_limit]
        chunk_text = tokenizer.decode(chunk_tokens)
        chunks.append(chunk_text)

    # Create a single DataFrame with all chunks
    df = pd.DataFrame(chunks, columns=["text"])

    return df


def add_embeddings_to_df(df):
    df["embedding"] = df.text.apply(
        lambda x: get_embedding(x, model="text-embedding-3-small")
    )
    return df
