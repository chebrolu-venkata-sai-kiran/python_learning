from openai import OpenAI
from dotenv import load_dotenv
import json
import time
import openai

load_dotenv()

client = OpenAI(
    api_key="AIzaSyAG5VdTALeVDZ7OM3XukRzqnWgrcPtEDsU",
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

# Global variables to track usage in the current session
session_tokens = 0

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

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]
user_query = input("Ask your question here 👉 ")
message_history.append({"role": "user", "content": user_query})

while True:
    try:
        response = client.chat.completions.create(
            model="gemini-2.0-flash",
            response_format={"type": "json_object"},
            messages=message_history
        )
        
        # --- TOKEN COUNTER LOGIC ---
        usage = response.usage
        prompt_tks = usage.prompt_tokens
        completion_tks = usage.completion_tokens
        total_tks = usage.total_tokens
        session_tokens += total_tks

        print(f"--- 📊 Token Usage: Input: {prompt_tks} | Output: {completion_tks} | Total: {total_tks} ---")
        # ---------------------------

        raw_result = response.choices[0].message.content
        message_history.append({"role": "assistant", "content": raw_result})
        parsed_result = json.loads(raw_result)

        step = parsed_result.get("step") or parsed_result.get("Step")
        content = parsed_result.get("content") or parsed_result.get("CONTENT")

        if step == "START":
            print(f"✅-> {content}")
        elif step == "PLAN":
            print(f"🧠 {content}")
        elif step == "OUTPUT":
            print(f"🤖 {content}")
            print(f"🏁 Session Finished. Total Tokens used: {session_tokens}")
            break
        
        # Sleep to respect the 5 RPM limit
        time.sleep(12)

    except openai.RateLimitError:
        print("⏳ Rate limit hit. Sleeping for 15 seconds...")
        time.sleep(40)
    except Exception as e:
        print(f"❌ Error: {e}")
        break