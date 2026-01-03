from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
api_key="AIzaSyAeRJB3aVS0Ntg-cxBOQ-uYBjw8hGS7wOc",
base_url="https://generativelanguage.googleapis.com/v1beta/")


response = client.chat.completions.create(
model="gemini-2.5-flash",
messages=[
    { "role": "system", "content": "you are an expert in the AI domain and only answer to the questions realted to the AI .if the query is not realted to AI just say sorry and do not answer" },
    { "role": "user", "content": "how many days need to learn about AI" }

    ]

)

print(response.choices [0].message.content)