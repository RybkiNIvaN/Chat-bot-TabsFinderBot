import os
import ords
import transliterate
import removing_letters
from transliterate import translit


def first_letter_number(your_group):
    return ords.first_letters_dict[your_group[0].lower()]


def go_to_firstletter_path(my_path, letter_number):
    next_path = letter_number
    os.chdir(os.path.join(my_path, str(next_path)))


def all_finder(my_path, what_to_find, group_or_song):
    what_to_find = removing_letters.remove_letters(what_to_find)
    what_to_find = translit(what_to_find, language_code='ru', reversed=True)
    print('4.1', what_to_find)
    to_find = what_to_find.split()
    list_of_sets = []

    def set_generator(to_find):
        my_set = set()
        for j in os.listdir(my_path):
            if to_find in j: my_set.add(j)
        return my_set

    for k in to_find:
        list_of_sets.append(set_generator(k))

    print('4.2', list_of_sets)
    if list_of_sets == [set()]:
        return list_of_sets
    final_set = set(list_of_sets[0])
    for i in range(1, len(list_of_sets)-1):
        final_set = final_set.intersection(list_of_sets[i])
        print(final_set)
    final = list(final_set)
    print('4.3', final[0])
    if group_or_song == 'group':
        os.chdir(os.path.join(my_path, str(final[0])))
        return str(final[0])
    elif group_or_song == 'song':
        return str(final[0])

