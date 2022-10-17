from multiprocessing.connection import Listener
import speech_recognition as sr

Listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        voice = Listener.listen(source)
        rec = Listener.recognize_google(voice)
        print(rec)

except:
    pass