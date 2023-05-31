def remove_letters(word):
    rm_list = ['ь', 'ая', 'я', 'ж', 'ш', 'ч', 'ый', 'ъ', 'й', 'ы', 'ю']
    for i in word:
        if i in rm_list: word =  word.replace(i, ' ')
    return word