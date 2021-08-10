import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    sample = rec.listen(source)

print(rec.recognize_google(sample))