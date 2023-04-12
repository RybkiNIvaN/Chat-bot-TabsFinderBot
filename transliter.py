import os
import ords
import main
import transliterate
from transliterate import translit
lang = 'ru'
your_group = 'Король и шут'
def first_letter_number(your_group):
    return ords.first_letters_dict[your_group[0]]

def go_to_firstletter_path(my_path, letter_number, lang):
    if lang == 'en':
        next_path = letter_number
        os.chdir(os.path.join(my_path, str(next_path)))
    elif lang == 'ru':
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
    #print(list_of_sets)

    final_set = set(list_of_sets[0])

    for i in range(1,len(list_of_sets)):
        final_set = final_set.intersection(list_of_sets[i])
    #if len(list_of_sets) == 1: return final_set
    #else:
        #final_set = final_set.intersection(list_of_sets[1])
        #for k in range(len(list_of_sets)):
            #final_set =
    return final_set



os.chdir(r"C:\Users\steve\PycharmProjects\pythonProject1\For_Project\Tabs")
print(os.getcwd())
my_path = os.getcwd()
go_to_firstletter_path(my_path, first_letter_number(your_group), lang)
my_path = os.getcwd()
your_group = translit(your_group, language_code='ru', reversed=True)
print(group_finder(my_path, your_group))
#print(os.listdir(my_path))
#print(os.getcwd())