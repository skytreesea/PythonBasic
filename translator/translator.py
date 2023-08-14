# pip install googletrans==4.0.0-rc1

from googletrans import Translator
def translate_text(text, target_lang='ko'):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, dest=target_lang)
    return translation.text
text = '''26:09 Robinson right uh you have a science fiction uh
26:15 Trope yeah yeah yeah I know I think that uh you know I mean I always thought
26:22 things like uh you know the queen and so on were very no
26:29 good novelist to read it's a point you share with uh it's a big science fiction
26:35 fact okay um okay I wanted to ask you one of the books that you wrote when you were back
26:40 in England I believe when you spent time in Oxford was Justice nature and the politics geography of difference
26:47 geography of difference um uh and I mean there's a lot of stuff in
26:52 that book it's it's quite a it's quite a rich uh book but one of the
26:59 things that you're working on is is the issue of um the ecological and it's a book that you
27:05 wrote in 1996 yeah so um before the sort of wave of eco-marxism
27:13 um and I'm surprised that it's some that's the whole issue about um ecology is not something you
27:19 particularly returned to since that book um uh or maybe I'm being unfair but uh'''
print(translate_text(text))