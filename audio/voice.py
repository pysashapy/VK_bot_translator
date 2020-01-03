import pyttsx3

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию

tts.setProperty('voice', 'ru')

# Попробовать установить предпочтительный голос

for voice in voices:
    print(voice)
    if voice.name == 'Irina':


        tts.setProperty('voice', voice.id)

tts.say('hello.')

tts.runAndWait()
