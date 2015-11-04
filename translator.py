import goslate
def Translate(word):
    gs = goslate.Goslate()
    translate_word=gs.translate(word, 'en')
    return translate_word
