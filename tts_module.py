# tts_module.py

import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)      # Speech speed
    engine.setProperty('volume', 1.0)    # Volume (0.0 to 1.0)

    engine.say(text)
    engine.runAndWait()
