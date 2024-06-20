from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Create
client.fine_tuning.jobs.create(training_file="data/all.json", model="gpt-3.5-turbo")
