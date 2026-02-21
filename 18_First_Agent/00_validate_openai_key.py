import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.responses.create(
        model="gpt-4",
        input="Say hello in one sentence."
    )

    print("Response:")
    print(response.output_text)

except Exception as e:
    print("Error occurred:")
    print(e)
