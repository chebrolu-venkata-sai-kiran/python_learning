from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import json
import time
import requests
import subprocess
from pydantic import BaseModel, Field
from typing import Optional
import os
import speech_recognition as sr
import asyncio
from openai.helpers import LocalAudioPlayer
from openai import AsyncOpenAI

async_client = AsyncOpenAI()
client = OpenAI()


async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts',
        voice='coral',
        instructions='Always speak in cheerful manner',
        input=speech,
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)


def run_command(command: str) -> str:
    """Runs a system command and returns stdout/stderr. WARNING: arbitrary command execution."""
    try:
        r = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        out = (r.stdout or "").strip() or "(no output)"
        err = (r.stderr or "").strip()
        if r.returncode != 0:
            return f"Exit code {r.returncode}. stdout: {out}. stderr: {err}"
        return out
    except subprocess.TimeoutExpired:
        return "Command timed out after 30 seconds."
    except Exception as e:
        return f"Command failed: {e}"


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "something went wrong"


available_tools = {
    "get_weather": get_weather,
    "run_command": run_command,
}


SYSTEM_PROMPT = """

you are an expert AI Assistant in resolving the user queries using chain of thought. your name is coder_AI
You work on the START, PLAN, TOOL and OUTPUT steps.
you need to first plan what needs to be done. the plan can be multiple steps
once you think enough plan has been done finally you can give me the output
you can also call a tool if required from the list of the available tools.
for every tool call wait for the observe step which is output of tool call.

Rule:
-Strictly follow the given json output format
-only run one step at a time
- the sequence of the steps is START (where user gives an input), PLAN (that can be multiple times) and finally OUTPUT (which is going to be the output to the user)

Output Json Format:
{
  "Step" : "START" or "PLAN" or "OUTPUT" or "TOOL",
  "content" : "string",
  "tool": "string",
  "input": "string",
  "output": "string"  # if this is a tool call, this will be the output of the tool
}

Available Tools:
- get_weather : takes city name as an input string and returns the weather about it
- run_command(command : str) : Takes a system command as string, executes it, and returns the command output (stdout)

Examples 01:
START: Hey, Can you solve 2 + 3 * 5 / 10
PLAN: { "step": "PLAN", "content": "Seems like user is interested in math problem" }
PLAN: { "step": "PLAN", "content": "looking at the problem, we should solve this using BODMAS method" }
PLAN: { "step": "PLAN", "content": "Yes, The BODMAS is correct thing to be done here" }
PLAN: { "step": "PLAN", "content": "first we must multiply 3 * 5 which is 15" }
PLAN: { "step": "PLAN", "content": "Now the new equation is 2 + 15 / 10" }
PLAN: { "step": "PLAN", "content": "We must perform divide that 15/10 = 1.5" }
PLAN: { "step": "PLAN", "content": "We must perform add now that 2+1.5 = 3.5" }
PLAN: { "step": "OUTPUT", "content": "the final ans is 3.5" }

Examples 02:
START: what is the weather of the delhi
PLAN: { "step": "PLAN", "content": "Seems like user is interested in weather of Delhi" }
PLAN: { "step": "PLAN", "content": "We have get_weather tool in the available tools" }
PLAN: { "step": "PLAN", "content": "I need to call get_weather with input delhi" }
PLAN: { "step": "TOOL", "tool": "get_weather", "input": "delhi" }
(OBSERVE is injected by system with tool output)
PLAN: { "step": "PLAN", "content": "Great I have the weather info for Delhi" }
PLAN: { "step": "OUTPUT", "content": "The current weather of Delhi is 20 C with cloudy sky" }

"""


class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Examples: START, PLAN, OUTPUT, TOOL, etc.")
    content: Optional[str] = Field(None, description="The content of the step.")
    tool: Optional[str] = Field(None, description="The tool used in this step.")
    input: Optional[str] = Field(None, description="The input params for the tool in this step.")


message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]


r = sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 2
            print("Say something!")
            audio = r.listen(source)
            print("Processing audio ...")
            user_query = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio. Try again.")
        continue
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}. Check network or API.")
        continue

    message_history.append({"role": "user", "content": user_query})

    while True:
        response = client.chat.completions.parse(
            model="gpt-4o-mini",
            response_format=MyOutputFormat,
            messages=message_history,
        )

        raw_result = response.choices[0].message.parsed
        message_history.append({"role": "assistant", "content": raw_result.model_dump_json()})
        parsed_result = response.choices[0].message.parsed

        if parsed_result.step == "START":
            time.sleep(5)
            print("✅", parsed_result.content)
            continue

        if parsed_result.step == "TOOL":
            tool_to_call = parsed_result.tool
            tool_input = parsed_result.input or ""
            if not tool_to_call or tool_to_call not in available_tools:
                tool_response = f"Unknown or missing tool: {tool_to_call}. Available: {list(available_tools)}"
            else:
                try:
                    tool_response = available_tools[tool_to_call](tool_input)
                except Exception as e:
                    tool_response = f"Tool error: {e}"
            print(f"⛏️: {tool_to_call} ({tool_input}) = {tool_response}")
            message_history.append({"role": "user", "content": json.dumps(
                {"step": "OBSERVE", "tool": tool_to_call, "input": tool_input, "output": tool_response}
            )})
            continue

        if parsed_result.step == "PLAN":
            time.sleep(5)
            print("🧠", parsed_result.content)
            continue

        if parsed_result.step == "OUTPUT":
            time.sleep(5)
            print("🤖", parsed_result.content)
            asyncio.run(tts(parsed_result.content or ""))
            break
