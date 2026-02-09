import speech_recognition as sr
import asyncio
from dotenv import load_dotenv
load_dotenv()

from openai.helpers import LocalAudioPlayer

from openai import OpenAI
from openai import AsyncOpenAI

client = OpenAI()
async_client = AsyncOpenAI()


async def tts(spech:str):
    async with async_client.audio.speech.with_streaming_response.create(
        model='gpt-4o-mini-tts',
        voice='coral',
        instructions='Always speak in cheefull manner',
        input=spech,
        response_format="pcm",

    ) as response:
        await LocalAudioPlayer().play(response)
        


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2
        SYSTEM_PROMPT = f"""
            you are an advanced voice agent you are given the transcript of what user said using voice.
            you need to output as if if you are an voice agent and whatever the responce we got will be converted back to the Audio using AI and played
            back to user. 
            """

        messages  = [{"role":"system","content": SYSTEM_PROMPT}]

        while True:


            print("Say something!")
            audio = r.listen(source)

            print("processing audio ...")
            stt = r.recognize_google(audio)

            print("you said: ", stt)
            messages.append({"role":"user","content":stt})

           

            response = client.chat.completions.create(
                model ="gpt-4.1-mini",
                messages=messages

            )
            print("Ai response",response.choices[0].message.content)
            asyncio.run(tts( spech=response.choices[0].message.content))

main()