import pyttsx3

VOICE_ZIRA = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
VOICE_HAZEL = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('voice', VOICE_ZIRA)


def tts_output(text):
    engine.say(text)
    engine.runAndWait()
