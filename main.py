import telebot
import config
import os
import transliter
<<<<<<< HEAD
<<<<<<< HEAD
import making_collection
=======
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> dbdbdf7bcae587bec984e69b0efa90430e17732b
from transliterate import translit
from telebot import types

bot = telebot.TeleBot(config.config['token'])
os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
my_path = os.getcwd()
<<<<<<< HEAD
<<<<<<< HEAD
my_answers = []  # 0 - название группы    1 - название песни    2 - файл песни

=======
my_answers = []  # 0 - язык    1 - название группы
>>>>>>> refs/remotes/origin/main

@bot.message_handler(commands=['start'])
def start(message):
<<<<<<< HEAD
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_collection = types.KeyboardButton('Открыть коллекцию')
    markup_reply.add(button_collection)
    bot.send_message(message.chat.id, 'Добро пожаловать, путник!', reply_markup=markup_reply)
    bot.send_message(message.chat.id, 'Чтобы найти музыкальную группу, введите /find')

=======
=======
my_answers = []  # 0 - язык    1 - название группы


@bot.message_handler(commands = ['start'])
def start(message):
>>>>>>> dbdbdf7bcae587bec984e69b0efa90430e17732b

    bot.send_message(message.chat.id, 'Добро пожаловать, путник!')
    bot.send_message(message.chat.id, 'Чтобы найти музыкальную группу, введите /find')

@bot.message_handler(commands = ['find'])
def get_lang_of_musicgroup(message):

    bot.send_message(message.chat.id, 'Введите название группы, только сначала скажите, группа носит название на русском языке или на английском')
    mess = bot.send_message(message.chat.id, 'en/ан - название на английском, ru/ру - на русском')
    os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
    print(os.getcwd())
    bot.register_next_step_handler(mess, get_musicgroup)
>>>>>>> refs/remotes/origin/main

@bot.message_handler(commands=['find'])
def get_musicgroup(message):
    my_answers.clear()
<<<<<<< HEAD
<<<<<<< HEAD
    os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
    print(os.getcwd())
=======
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> dbdbdf7bcae587bec984e69b0efa90430e17732b
    mess = bot.send_message(message.chat.id, 'Хорошо, песни какой группы хотите сыграть сегодня?')

    bot.register_next_step_handler(mess, your_group)


def your_group(message):
    my_answers.append(message.text)
<<<<<<< HEAD
<<<<<<< HEAD
    print(my_answers[0])
=======
=======

    print(my_answers[1])
    print(my_answers)
>>>>>>> dbdbdf7bcae587bec984e69b0efa90430e17732b

    print(my_answers[1])
>>>>>>> refs/remotes/origin/main
    print(my_answers)
    bot.send_message(message.chat.id, f'Будем искать группу {message.text}')
    my_path = os.getcwd()
<<<<<<< HEAD
<<<<<<< HEAD
    try:
        transliter.go_to_firstletter_path(my_path, transliter.first_letter_number(my_answers[0].lower()))
        my_path = os.getcwd()
        print(my_path)
        my_answers0_translite = translit(my_answers[0].lower(), language_code='ru', reversed=True)
        my_group = transliter.all_finder(my_path, my_answers0_translite, 'group')
        print(my_group)
        if my_group != set():
            bot.send_message(message.chat.id, f'Я нашел группу {my_answers[0]}, кстати, у меня есть {len(os.listdir())} файла/ов')
        print(os.getcwd())
        print(os.listdir())
        mess = bot.send_message(message.chat.id, 'Какую композицию мне найти?')
        bot.register_next_step_handler(mess, your_song)
    except FileNotFoundError as no_group:
        except_mess = bot.send_message(message.chat.id, "Группа не найдена, введите снова /find")
        bot.clear_step_handler_by_chat_id(message.chat.id)


def your_song(message):
    my_path = os.getcwd()
    my_answers.append(message.text)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сохранить в коллекцию", callback_data='save')
    markup.add(button1)
    try:
        my_file = transliter.all_finder(my_path, my_answers[1].lower(), 'song')
        print(my_file)
        if my_file != set():
            my_answers.append(my_file)
            bot.send_message(message.chat.id, f'Я нашел композицию {my_answers[1]}', reply_markup=markup)
            song_my_file = open(my_file, 'rb')
            bot.send_document(message.chat.id, song_my_file)

            @bot.callback_query_handler(func=lambda call: True)
            def callback(call):
                if call.message:
                    if call.data == 'save':
                        print(message.from_user.username)
                        making_collection.add_to_collection(message.from_user.username, my_answers[2], os.getcwd())
                        bot.send_message(message.chat.id, 'Файл сохранен в коллекцию')
                        bot.clear_step_handler_by_chat_id(message.chat.id)
    except FileNotFoundError as no_song:
        except_mess = bot.send_message(message.chat.id, "Песня не найдена, введите снова /find")
        bot.clear_step_handler_by_chat_id(message.chat.id)
    except IndexError as empty_sets:
        except_mess = bot.send_message(message.chat.id, "Песня не найдена, введите снова /find")
        bot.clear_step_handler_by_chat_id(message.chat.id)
    except Exception as empty_file:
        except_mess = bot.send_message(message.chat.id, "Файл пустой")
        bot.clear_step_handler_by_chat_id(message.chat.id)


@bot.message_handler(content_types=['text'])
def text_func(message):
    if message.text == 'Открыть коллекцию':
        inline_markup_2 = types.InlineKeyboardMarkup(row_width=2)
        button_open_collection = types.InlineKeyboardButton('Открыть всю коллекцию', callback_data= 'open_collection')
        button_open_file_in_collection = types.InlineKeyboardButton('Открыть файл из коллекции', callback_data= 'open_file')
        inline_markup_2.add(button_open_collection, button_open_file_in_collection)
        bot.send_message(message.chat.id, f'В вашей коллекции {making_collection.go_to_collection(message.from_user.username)} файла/ов', reply_markup= inline_markup_2)

        @bot.callback_query_handler(func=lambda call: True)
        def callback(call):
            if call.message:
                if call.data == 'open_collection':
                    bot.send_message(message.chat.id, making_collection.open_all_collection())
                if call.data == 'open_file':
                    mess = bot.send_message(message.chat.id, 'Какой файл из коллекции вы хотите скачать?')
                    bot.register_next_step_handler(mess, file_open)

        def file_open(message):
            try:
                file_from_collection = transliter.all_finder(os.getcwd(), message.text, 'song')
                file_to_open = open(file_from_collection, 'rb')
                bot.send_document(message.chat.id, file_to_open)
            except Exception as file_error:
                bot.send_message(message.chat.id, "Файл в коллекции не найден")

try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass
=======
    transliter.go_to_firstletter_path(my_path, transliter.first_letter_number(my_answers[1].lower()), my_answers[0])
    my_path = os.getcwd()
=======
    transliter.go_to_firstletter_path(my_path, transliter.first_letter_number(my_answers[1].lower()), my_answers[0])
    my_path = os.getcwd()
>>>>>>> dbdbdf7bcae587bec984e69b0efa90430e17732b

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
>>>>>>> refs/remotes/origin/main
