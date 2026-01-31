from openai import OpenAI
from dotenv import load_dotenv
import json
import time
import requests

load_dotenv()
client = OpenAI()
#chain of thought 

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response =  requests.get(url)
    if response.status_code == 200:
        weather_data = response.text 
        return weather_data
    return "something went wrong"

available_tools = {
    "get_weather": get_weather
}



SYSTEM_PROMPT = """

you are an expert AI Assistant in resolving the user queries using chain of thought. your name is coder_AI 
You work on the START,PLAN ,TOOL and OUTPUT steps.
you need to first plan what needs to be done.the plan can be multiple steps 
once you think enought plan has been done finally you can give me the output
you can also call a tool if required from the list of the available tools.
for every tool call wait for the observe step which is output of tool call.


Rule:
-Strictly follow the give json output format 
-only run one steps at a time 
- the sequence of the steps is START (where user gives an input),PLAN (that can be multiple times ) and finally OUTPUT (which sis goint to be the output to the user)

Output Json Format:
{
"Step" : "START" or "PLAN" or "OUTPUT or TOOL",
"content" : "string",
"tool": "string",
"input": "string",
"output": "string"  # if this is a tool call, this will be the output of the tool
}

Available Tools:
- get_weather : takes city name as an input string and returns the weather about it 

Examples 01:
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



Examples 02:
START: what is the weather of the delhi
PLAN: { "step": "PLAN": "content": "Seems like user is interested weather of the delhi" }
PLAN: { "step": "PLAN": "content": "let see if we have available tools for the list of the available tools" }
PLAN: { "step": "PLAN": "content": "Great we have get_weather tool for this query " }
PLAN: { "step": "PLAN": "content": "i need to call get_weather tool for delhi as input for city " }
PLAN: { "step": "TOOL": "tool":"get_weather" , "input": "delhi"}
PLAN: { "step": "OBSERVE": "tool":"get_weather" , "output": "the temperature of the delhi is 20 C"}
PLAN: { "step": "PLAN": "content": "Great i have the weather info for the delhi "}
PLAN: { "step": "OUTPUT": "content": "the current weather of the delhi is 20 C with cloudy sky"}


"""

message_history = [
    { "role": "system", "content":SYSTEM_PROMPT},

]
while True:
    user_query = input("Ask your question here 👉")

    message_history.append({ "role": "user", "content": user_query })

    while True:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            response_format={"type":"json_object"},
            messages=message_history)

        raw_result  = response.choices [0].message.content
        message_history.append({"role": "assistant","content":raw_result})
        parsed_result = json.loads(raw_result)

        if parsed_result["Step"] == "START":
            time.sleep(5)
            print("✅",parsed_result.get("content"))
            continue

        if parsed_result["Step"] == "TOOL":
            tool_to_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")
            print(f"⛏️: {tool_to_call} ({tool_input})")

            tool_response = available_tools[tool_to_call](tool_input)
            print(f"⛏️: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({"role": "developer", "content": json.dumps(
                {"step": "OBSERVE","tool":tool_to_call,  "input" : tool_input , "output": tool_response}
                )}) 
            continue

        if parsed_result["Step"] == "PLAN":
            time.sleep(5)
            print("🧠",parsed_result.get("content"))
            continue

        if parsed_result["Step"] == "OUTPUT":
            time.sleep(5)
            print("🤖",parsed_result.get("content"))

            break
        

