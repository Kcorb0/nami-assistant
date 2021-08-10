from posixpath import split
import speech_recognition as sr
from program_interaction.open_app import open_app

def get_mic_audio(recognizer, microphone):
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=.5)
        sample = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(sample)
    except sr.UnknownValueError:
        text = 'Not sure what you said? Try again.'

    return text


rec = sr.Recognizer()
mic = sr.Microphone()
run = True


while run:

    gen_text = get_mic_audio(rec, mic).lower()
    stop_words = ['end', 'stop', 'cancel', 'terminate']


    if gen_text in stop_words:
        run = False

    elif 'open' in gen_text:
        split_text = gen_text.split('open ')

        if len(split_text) > 1:
            app = split_text[1].title()
            print(f'opening {app}')
            open_app(app)

    else:
        print(gen_text)
