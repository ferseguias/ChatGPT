import openai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("openai_api_key")

openai.api_key = api_key

while True:

    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)
    
    print(completion.choices[0].text)