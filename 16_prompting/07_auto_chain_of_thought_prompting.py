from openai import OpenAI
from dotenv import load_dotenv
import json
import time

load_dotenv()

client = OpenAI(
api_key="AIzaSyAG5VdTALeVDZ7OM3XukRzqnWgrcPtEDsU",
base_url="https://generativelanguage.googleapis.com/v1beta/")
#chain of thought 





SYSTEM_PROMPT = """

you are an expert in the coding domain and only answer to the questions realted to the coding. your name is coder_AI 
You work on the START,PLAN and OUTPUT steps.
you need to first plan what needs to be done.the plan can be multiple steps 
once you think enought plan has been done finally you can give me the output


Rule:
-Strictly follow the give json output format 
-only run one steps at a time 
- the sequence of the steps is START (where user gives an input),PLAN (that can be multiple times ) and finally OUTPUT (which sis goint to be the output to the user)

Output Format:
{
"Step" : "START" or "PLAN" or "OUTPUT",
"content" : "string"
}

Examples:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN": "content": "Seems like user is interested in math
problem" }
PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve
this using BODMAS method" }
PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be
done here" }
PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is
15" }
PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10"}
PLAN: { "step": "PLAN": "content": "We must perform divide that 15/10 = 1.5"}
PLAN: { "step": "PLAN": "content": "We must perform add now that 2+1.5 = 3.5"}
PLAN: { "step": "OUTPUT": "content": "the final ans is 3.5"}






"""

message_history = [
    { "role": "system", "content":SYSTEM_PROMPT},

]

user_query = input("Ask your question here 👉")

message_history.append({ "role": "user", "content": user_query })

while True:
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        response_format={"type":"json_object"},
        messages=message_history)
    
    raw_result  = response.choices [0].message.content
    message_history.append({"role": "assistant","content":raw_result})
    parsed_result = json.loads(raw_result)

    if parsed_result["Step"] == "START":
        time.sleep(5)
        print("✅",parsed_result.get("content"))
        continue

    if parsed_result["Step"] == "PLAN":
        time.sleep(5)
        print("🧠",parsed_result.get("content"))
        continue

    if parsed_result["Step"] == "OUTPUT":
        time.sleep(5)
        print("🤖",parsed_result.get("content"))

        break
    

