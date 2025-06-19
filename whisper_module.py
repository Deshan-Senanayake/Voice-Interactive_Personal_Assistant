# whisper_module.py

import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

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


from faster_whisper import WhisperModel

def load_whisper_model(model_size="base"):
    print("🧠 Loading Whisper model (CPU mode)...")
    model = WhisperModel(model_size, device="cpu", compute_type="int8_float32")
    return model



def transcribe_audio_with_model(model, filename="input.wav"):
    """
    Transcribes audio using a preloaded Whisper model.

    Args:
        model (WhisperModel): Loaded Whisper model
        filename (str): Path to audio file

    Returns:
        str: Transcribed text
    """
    print(f"🧠 Transcribing {filename}...")
    segments, _ = model.transcribe(filename)

    transcription = " ".join(segment.text.strip() for segment in segments)
    print(f"📝 Transcription: {transcription}")
    return transcription.strip()
