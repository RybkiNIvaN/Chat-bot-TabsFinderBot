<<<<<<< HEAD
<<<<<<< HEAD
def remove_letters(word):
    if 'ь' in word: word = word.replace('ь', ' ')

    if 'ая' in word:
        word = word.replace('ая', ' ')
    elif 'я' in word:
        word = word.replace('я', ' ')

    if 'ж' in word: word = word.replace('ж', ' ')

    if 'ч' in word: word = word.replace('ч', ' ')

    if 'ш' in word: word = word.replace('ш', ' ')

    if 'ый' in word:word = word.replace('ый', ' ')
    elif 'й' in word: word = word.replace('й', ' ')
    elif 'ы' in word: word = word.replace('ы', ' ')

    if 'ъ' in word:
        word = word.replace('ъ', ' ')

=======
def remove_letters(word):
    if 'ь' in word: word = word.replace('ь', ' ')

    if 'ая' in word:
        word = word.replace('ая', ' ')
    elif 'я' in word:
        word = word.replace('я', ' ')

    if 'ж' in word: word = word.replace('ж', ' ')

    if 'ч' in word: word = word.replace('ч', ' ')

    if 'ш' in word: word = word.replace('ш', ' ')

    if 'ый' in word:word = word.replace('ый', ' ')
    elif 'й' in word: word = word.replace('й', ' ')
    elif 'ы' in word: word = word.replace('ы', ' ')

    if 'ъ' in word:
        word = word.replace('ъ', ' ')

>>>>>>> refs/remotes/origin/main
=======
def remove_letters(word):
    if 'ь' in word: word = word.replace('ь', ' ')

    if 'ая' in word:
        word = word.replace('ая', ' ')
    elif 'я' in word:
        word = word.replace('я', ' ')

    if 'ж' in word: word = word.replace('ж', ' ')

    if 'ч' in word: word = word.replace('ч', ' ')

    if 'ш' in word: word = word.replace('ш', ' ')

    if 'ый' in word:word = word.replace('ый', ' ')
    elif 'й' in word: word = word.replace('й', ' ')
    elif 'ы' in word: word = word.replace('ы', ' ')

    if 'ъ' in word:
        word = word.replace('ъ', ' ')

>>>>>>> dbdbdf7bcae587bec984e69b0efa90430e17732b
    return word