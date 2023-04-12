import telebot
import config
import ords
import os
import transliterate
from transliterate import translit
from telebot import types

bot = telebot.TeleBot(config.config['token'])
os.chdir(r"C:\Users\steve\PycharmProjects\pythonProject1\For_Project\Tabs")
my_path = os.getcwd()
my_answers = [] # 0 - язык    1 - название группы
def go_to_firstletter_path(my_path, letter_number, lang):
    if lang == 'en':
        next_path = letter_number
        os.chdir(os.path.join(my_path, str(next_path)))
    elif lang == 'ru':
        next_path = letter_number
        os.chdir(os.path.join(my_path, str(next_path)))

def first_letter_number(your_group):
    return ords.first_letters_dict[your_group[0]]

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

    final_set = set(list_of_sets[0])

    for i in range(1, len(list_of_sets)):
        final_set = final_set.intersection(list_of_sets[i])

    return final_set



@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать, путник!')
    bot.send_message(message.chat.id, 'Чтобы найти музыкальную группу, введите /find')

@bot.message_handler(commands = ['find'])
def get_lang_of_musicgroup(message):
    bot.send_message(message.chat.id, 'Введите название группы, только сначала скажите, группа носит название на русском языке или на английском')
    mess = bot.send_message(message.chat.id, 'en - название на английском, ru - на русском')


    bot.register_next_step_handler(mess, get_musicgroup)

def get_musicgroup(message):
    mess = bot.send_message(message.chat.id, 'Хорошо, песни какой группы хотите сыграть сегодня?')
    my_answers.append(message.text.lower())
    print(my_answers[0])
    bot.register_next_step_handler(mess, your_group)

def your_group(message):
    my_answers.append(message.text)
    print(my_answers[1])
    print(my_answers)

    bot.send_message(message.chat.id, f'Будем искать группу {message.text}')
    my_path = os.getcwd()
    go_to_firstletter_path(my_path,first_letter_number(my_answers[1]), my_answers[0])
    my_path = os.getcwd()
    print(my_path)
    my_answers1_translite = translit(my_answers[1], language_code='ru', reversed=True)
    my_group = group_finder(my_path, my_answers1_translite)
    print(my_group)
    if my_group != set(): bot.send_message(message.chat.id, f'Я нашел группу {my_answers[1]}')



























bot.polling(none_stop=True)
