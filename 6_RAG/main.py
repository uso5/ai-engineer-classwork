from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
from prepare_data import prepare_tweet_data, add_embeddings_to_df
from search import search_text
from call_openai import create_prompt, query_openai_chat

_ = load_dotenv(find_dotenv())

prompt = "Help me write tweet about chatbots and self-driving cars."


def main():
    datafile_path = "data/input_output.txt"
    df = prepare_tweet_data(datafile_path)
    
    df = add_embeddings_to_df(df)

    # # # Search for relevant context
    search_results = search_text(df, prompt, n=3)

    print("Search results:", search_results["text"])

    # # # Create the prompt
    final_prompt = create_prompt(search_results["text"], prompt)

    print("Final prompt:", final_prompt)

    # # # Send the query to OpenAI
    response = query_openai_chat(final_prompt)
    print("OpenAI's response:", response)


if __name__ == "__main__":
    main()