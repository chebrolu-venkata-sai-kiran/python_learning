# Chapter 25 – Voice Agents

Voice-based agent: speech-to-text → LLM + tools → text-to-speech.

## Requirements

- **OpenAI API key** in `.env` as `OPENAI_API_KEY`
- **Microphone** and **speakers** for STT/TTS
- **PyAudio** / **sounddevice** and **SpeechRecognition** (see root `requirements.txt`)

## Run

- `python main.py` – Main voice flow entry point.
- `python cursor_fixed.py` or `python cursor.py` – Full agent loop with tools (weather, run_command) and async TTS.

## Tools

The agent can call:

- **get_weather(city)** – Weather for a city (wttr.in).
- **run_command(command)** – Runs a system command (use with care).

## Note

TTS uses OpenAI streaming audio with `LocalAudioPlayer`; ensure your environment supports playback.
