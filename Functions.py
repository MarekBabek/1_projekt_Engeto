#funkce pro rozdělení vět v listu (zanořené)
def split_list(sentence):
    separated_texts = []
    for TEXTS in sentence:
        separated_texts.append(TEXTS.split())
    return separated_texts

# funkce pro nahrazení hvězdami namísto délky stringu
def asterisks_replace_x(word):
    return '*' * word

