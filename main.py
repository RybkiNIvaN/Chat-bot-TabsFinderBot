import telebot
import config
import ords
import os
import transliter
from transliterate import translit
from telebot import types

bot = telebot.TeleBot(config.config['token'])
os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
my_path = os.getcwd()
my_answers = []  # 0 - язык    1 - название группы


@bot.message_handler(commands = ['start'])
def start(message):

    bot.send_message(message.chat.id, 'Добро пожаловать, путник!')
    bot.send_message(message.chat.id, 'Чтобы найти музыкальную группу, введите /find')

@bot.message_handler(commands = ['find'])
def get_lang_of_musicgroup(message):

    bot.send_message(message.chat.id, 'Введите название группы, только сначала скажите, группа носит название на русском языке или на английском')
    mess = bot.send_message(message.chat.id, 'en/ан - название на английском, ru/ру - на русском')
    os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
    print(os.getcwd())
    bot.register_next_step_handler(mess, get_musicgroup)

def get_musicgroup(message):
    my_answers.clear()
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
    transliter.go_to_firstletter_path(my_path, transliter.first_letter_number(my_answers[1].lower()), my_answers[0])
    my_path = os.getcwd()

    print(my_path)

    if 'ь' in my_answers[1]:
        my_answers_removed = my_answers[1].replace('ь', '')
        my_answers1_translite = translit(my_answers_removed.lower(), language_code='ru', reversed=True)
        my_group = transliter.group_finder(my_path, my_answers1_translite)
    else:
        my_answers1_translite = translit(my_answers[1].lower(), language_code='ru', reversed=True)
        my_group = transliter.group_finder(my_path, my_answers1_translite)


    print(my_group)
    if my_group != set():
        bot.send_message(message.chat.id, f'Я нашел группу {my_answers[1]}, кстати, у меня есть {len(os.listdir())} файлов')
    print(os.getcwd())
    print(os.listdir())
    mess = bot.send_message(message.chat.id, 'Какую композицию мне найти?')
    bot.register_next_step_handler(mess, your_song)

def your_song(message):
    my_path = os.getcwd()
    my_answers.append(message.text)
    file = transliter.song_finder(my_path, my_answers[2].lower())
    print(file)







bot.polling(none_stop=True)
