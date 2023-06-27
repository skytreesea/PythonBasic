# pip install googletrans==4.0.0-rc1

from googletrans import Translator
def translate_text(text, target_lang='en'):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=target_lang)
    return translation.text

translate_text('나는 네가 행복하기를 원한다. ')