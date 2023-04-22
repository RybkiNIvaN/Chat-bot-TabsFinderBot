import os
import ords
import transliterate
from transliterate import translit

def first_letter_number(your_group):
    return ords.first_letters_dict[your_group[0].lower()]

def go_to_firstletter_path(my_path, letter_number, lang):
    if lang == 'en' or 'ан':
        next_path = letter_number
        os.chdir(os.path.join(my_path, str(next_path)))
    elif lang == 'ru' or 'ру':
        next_path = letter_number
        os.chdir(os.path.join(my_path, str(next_path)))

def group_finder(my_path, your_group):

    group = your_group.split()
    list_of_sets = []
    def set_generator(group):
        my_set = set()
        for j in os.listdir(my_path):
            if group in j: my_set.add(j)
        return my_set
    for k in group:
        list_of_sets.append(set_generator(k))

    print(list_of_sets)
    final_set = set(list_of_sets[0])

    for i in range(1, len(list_of_sets)):
        final_set = final_set.intersection(list_of_sets[i])

    return final_set




