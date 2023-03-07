def decryption(message):
    translated = ""
    for i_word in message:
        if i_word in letters:
            num_index = letters.find(i_word)
            translated += letters[num_index - 1]
        else:
            translated += i_word
    return translated


def shift(text, key):
    word_ln = len(text)
    shift = key % word_ln
    text = text[-shift:] + text[:-shift]
    return text


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/' \
       'dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
       'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/' \
       'qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/' \
       'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /' \
       'ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
       'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

text_2 = []
key = 3
for i_word in text:
    text_decryption = decryption(i_word)
    shift_text = shift(text_decryption, key)
    if shift_text.endswith('/'):
        key += 1
        text_2.append(shift_text)
    else:
        text_2.append(shift_text)

text_2 = ' '.join(text_2)
text_2 = text_2.replace('+', '*')
text_2 = text_2.replace('-', ',')
text_2 = text_2.replace('(', "'")
text_2 = text_2.replace('..', '--')
text_2 = text_2.replace('"', '!')
text_2 = text_2.replace('/', '.\n')

print(text_2)
