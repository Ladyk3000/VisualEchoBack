from googletrans import Translator

translator = Translator()


def translate(text, target_lang="en"):
    result = translator.translate(text, dest=target_lang)
    return result.text
