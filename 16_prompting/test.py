from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Try explicit API key
client = OpenAI(api_key=os.getenv("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"))

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello, world!"}
        ],
        max_tokens=50
    )
    
    output_text = response.choices[0].message.content
    print(output_text)

except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Error details: {str(e)}")
