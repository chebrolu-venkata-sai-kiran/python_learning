from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import json
import time
import requests
from pydantic import BaseModel,Field
from typing import Optional
import os
import speech_recognition as sr
import asyncio
from openai.helpers import LocalAudioPlayer
from openai import AsyncOpenAI
async_client = AsyncOpenAI()


client = OpenAI()
#chain of thought 


async def tts(spech:str):
    async with async_client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts',
        voice='coral',
        instructions='Always speak in cheefull manner',
        input=spech,
        response_format="pcm",

    ) as response:
        await LocalAudioPlayer().play(response)

def run_command(command: str) -> str:
    result = os.system(command)
    return f"Command executed successfully with exit code {result}" if result == 0 else f"Command execution failed with exit code {result}"

def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response =  requests.get(url)
    if response.status_code == 200:
        weather_data = response.text 
        return weather_data
    return "something went wrong"

available_tools = {
    "get_weather": get_weather,
    "run_command": run_command
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
- run_command(command : str) : Takes a system linux command as string and excutes commands in the user system and return the output from that command

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

class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step in the conversation. Examples: START, PLAN, OUTPUT, TOOL,etc.")
    content: Optional[str] = Field(None, description="The content of the step in the conversation.")
    tool: Optional[str] = Field(None, description="The tool used in this step.")
    input: Optional[str] = Field(None, description="The input params for the tool in this step.")

message_history = [
    { "role": "system", "content":SYSTEM_PROMPT},

]


r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        print("Say something!")
        audio = r.listen(source)
        print("processing audio ...")
        user_query = r.recognize_google(audio)


        

        message_history.append({ "role": "user", "content": user_query })

        while True:
            response = client.chat.completions.parse(
                model="gpt-4o-mini",
                response_format=MyOutputFormat,
                messages=message_history)

            raw_result  = response.choices [0].message.parsed
            message_history.append({"role": "assistant","content": raw_result.model_dump_json()})
            parsed_result = response.choices [0].message.parsed


            if parsed_result.step == "START":
                time.sleep(5)
                print("✅",parsed_result.content)
                continue

            if parsed_result.step == "TOOL":
                tool_to_call = parsed_result.tool
                tool_input = parsed_result.input
                print(f"⛏️: {tool_to_call} ({tool_input})")

                tool_response = available_tools[tool_to_call](tool_input)
                print(f"⛏️: {tool_to_call} ({tool_input}) = {tool_response}")
                message_history.append({"role": "developer", "content": json.dumps(
                    {"step": "OBSERVE","tool":tool_to_call,  "input" : tool_input , "output": tool_response}
                    )}) 
                continue

            if parsed_result.step == "PLAN":
                time.sleep(5)
                print("🧠",parsed_result.content)
                continue

            if parsed_result.step == "OUTPUT":
                time.sleep(5)
                print("🤖",parsed_result.content)
                asyncio.run(tts( spech=parsed_result.content))

                break
        

