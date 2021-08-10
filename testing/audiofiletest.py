import speech_recognition as sr
from pprint import pprint


rec = sr.Recognizer()

testwav = sr.AudioFile('testing/vatest2.wav')

with testwav as source:
    rec.adjust_for_ambient_noise(source)
    test_audio = rec.record(source)

pprint(rec.recognize_google(test_audio, show_all=True))