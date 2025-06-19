# main.py

from whisper_module import record_audio, load_whisper_model, transcribe_audio_with_model
from llm_module import ask_ollama
from tts_module import speak_text

if __name__ == "__main__":
    model = load_whisper_model("base")   # 🔁 Only load once
    record_audio(duration=5)             # 🎙️ Record your voice
    query = transcribe_audio_with_model(model, "input.wav")  # 🧠 Transcribe
    print("🗨️ You said:", query)

    response = ask_ollama(query)         # 🤖 Get answer
    print("🧠 Assistant:", response)

    speak_text(response)                 # 🔊 Speak response
