import speech_recognition as sr
from settings.tts_output import tts_output

def get_mic_audio(recognizer, microphone):
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=.5)
        sample = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(sample)
    except sr.UnknownValueError:
        text = 'I could not process that, sorry. Speak again.'

    return text