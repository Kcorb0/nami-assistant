import speech_recognition as sr
from settings.get_mic_audio import get_mic_audio
from program_interaction.open_app import open_app
from general_interaction.date_and_time import get_date, get_time



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

    elif gen_text == 'date':
        print(get_date())

    elif gen_text == 'time':
        print(get_time())

    else:
        print(gen_text)
