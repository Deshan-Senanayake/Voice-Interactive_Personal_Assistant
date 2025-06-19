# whisper_module.py

import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="input.wav", duration=5, samplerate=16000):
    """
    Records audio from the microphone and saves it as a .wav file.

    Args:
        filename (str): Output filename
        duration (int): Duration in seconds
        samplerate (int): Sample rate (16000 recommended for Whisper)
    """
    print(f"🎙️ Recording for {duration} seconds... Speak now!")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    write(filename, samplerate, recording)
    print(f"✅ Saved recording to {filename}")
