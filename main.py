import speech_recognition as sr


def get_mic_audio(recognizer, microphone):
    
    with mic as source:
        rec.adjust_for_ambient_noise(source, duration=.5)
        sample = rec.listen(source)

    try:
        text = rec.recognize_google(sample)
    except sr.UnknownValueError:
        text = 'Not sure what you said? Try again.'

    return text


rec = sr.Recognizer()
mic = sr.Microphone()
run = True

while run:
    gen_text = get_mic_audio(rec, mic).lower()

    if gen_text == 'cloud':
        print('Yup there are clouds')
    elif gen_text == 'end':
        run = False
    else:
        print(gen_text)
    

