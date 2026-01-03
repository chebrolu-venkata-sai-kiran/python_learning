from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
api_key="AIzaSyAeRJB3aVS0Ntg-cxBOQ-uYBjw8hGS7wOc",
base_url="https://generativelanguage.googleapis.com/v1beta/")

# Few shot prompting: directly giving instructions to model and giving few examples 

SYSTEM_PROMPT = """

you are an expert in the coding domain and only answer to the questions realted to the coding. your name is coder_AI .if the query is not realted to coding just say sorry and do not answer

Rule:
-Strictly follow the output in the Json format

Output Format:
{
"code" : "string" or null,
"iscoding" : boolean
}

Examples:

Q: can you explain about the chemistry?
A: {
"code" :   null,
"iscoding" : False
}

Q: what is the weather like today?
A: {
"code" :   null,
"iscoding" : False
}

Q: write a code for a+b ?
A: {
"code" :   "def add(a,b):
return a+b ",
"iscoding" : True
}

"""


response = client.chat.completions.create(
model="gemini-2.5-flash",
messages=[
    { "role": "system", "content":SYSTEM_PROMPT},
    { "role": "user", "content": "write a code in java for palindrome" }

    ]

)

print(response.choices [0].message.content)