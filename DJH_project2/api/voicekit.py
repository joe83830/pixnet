from gtts import gTTS


def generate_audio(dish, path):

    lang = 'zh-tw'
    tts = gTTS(dish, lang=lang, lang_check=False)
    tts.save(path)
