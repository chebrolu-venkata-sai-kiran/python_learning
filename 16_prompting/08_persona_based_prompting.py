from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
api_key="AIzaSyAG5VdTALeVDZ7OM3XukRzqnWgrcPtEDsU",
base_url="https://generativelanguage.googleapis.com/v1beta/")


SYSTEM_PROMPT = """
You are an AI Persona Assistant named Sai Kiran
You are acting on behalf of Sai Kiran who is 25 years old Tech enthusiatic and Functional tester.
 Your main tech stack is Python and You are leaning GenAI these days.

 Examples:
Q. Hey
A: Hey, Tell Me!



"""


response = client.chat.completions.create(
model="gemini-2.5-flash",
messages=[
    { "role": "system", "content":SYSTEM_PROMPT},
    { "role": "user", "content": "Hey There" }

    ]

)

print(response.choices [0].message.content)