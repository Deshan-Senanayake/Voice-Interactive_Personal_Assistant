# main.py

from llm_module import ask_ollama
from tts_module import speak_text

# main.py

from whisper_module import record_audio

if __name__ == "__main__":
    record_audio(duration=5)  # You can adjust the time

