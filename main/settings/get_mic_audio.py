import speech_recognition as sr

def get_mic_audio(recognizer, microphone):
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=.5)
        sample = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(sample)
    except sr.UnknownValueError:
        text = 'Not sure what you said? Try again.'

    return text