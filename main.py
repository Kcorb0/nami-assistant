import speech_recognition as sr
import os


def get_mic_audio(recognizer, microphone):
    
    with mic as source:
        rec.adjust_for_ambient_noise(source, duration=.5)
        sample = rec.listen(source)

    try:
        text = rec.recognize_google(sample)
    except sr.UnknownValueError:
        text = 'Not sure what you said? Try again.'

    return text

def run_steam_game(library_loc):
    os.startfile(library_loc)


rec = sr.Recognizer()
mic = sr.Microphone()
run = True

game_location = 'A:/SteamLibrary/steamapps/common/RimWorld/RimWorldWin64.exe'

while run:
    gen_text = get_mic_audio(rec, mic).lower()
    
    stop_words = ['end', 'stop', 'cancel', 'terminate']

    if gen_text in stop_words:
        run = False
    elif gen_text == 'run rimworld':
        run_steam_game(game_location)
    else:
        print(gen_text)
    
