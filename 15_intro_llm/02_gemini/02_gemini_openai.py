from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
api_key="AIzaSyAeRJB3aVS0Ntg-cxBOQ-uYBjw8hGS7wOc",
base_url="https://generativelanguage.googleapis.com/v1beta/")


response = client.chat.completions.create(
model="gemini-2.5-flash",
messages=[
{ "role": "user", "content": "Hey, I am Kiran. Nice to meet you"}])



print(response.choices [0].message.content)