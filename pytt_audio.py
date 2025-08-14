import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 180)      # words per minute
    engine.setProperty("volume", 0.9)    # 0.0–1.0
    engine.say(text)
    engine.runAndWait()
