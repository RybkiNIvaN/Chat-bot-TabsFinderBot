import telebot
import config
import os
import database_main
import removing_letters
import transliter
from telebot import types

bot = telebot.TeleBot(config.config['token'])
os.chdir(r"C:\Users\steve\Chat-bot-TabsFinderBot\For_Project\Tabs")
my_path = os.getcwd()
my_answers = []  # 0 - название группы    1 - название песни
info = []  # 0 - группа на английском (my_group)    1 - файл песни


@bot.message_handler(commands=['find'])
def get_musicgroup(message):
    my_answers.clear()
    info.clear()
    print('0.1', message.from_user.username, message.from_user.id)
    os.chdir(r"C:\Users\steve\Chat-bot-TabsFinderBot")
    database_main.add_user(message.from_user.username, message.from_user.id)

    os.chdir("C:\\Users\\steve\\PycharmProjects\\pythonProject1\\For_Project\\Tabs")
    print('1', os.getcwd())
    mess = bot.send_message(message.chat.id, 'Хорошо, песни какой группы хотите сыграть сегодня?')

    bot.register_next_step_handler(mess, your_group)


def your_group(message):
    my_answers.append(message.text)
    print('2', my_answers[0])
    print('3', my_answers)
    if message.text ==r'/find':
        bot.send_message(message.chat.id, "Не надо вводить find сейчас")
        bot.clear_step_handler_by_chat_id(message.chat.id)
    else:
        bot.send_message(message.chat.id, f'Будем искать группу {message.text}')

    my_path = os.getcwd()
    try:
        transliter.go_to_firstletter_path(my_path, transliter.first_letter_number(my_answers[0].lower()))
        my_path = os.getcwd()
        print('4', my_path)
        my_group = transliter.all_finder(my_path, removing_letters.remove_letters(my_answers[0].lower()), 'group')
        print('5', my_group)
        if my_group != set():
            info.append(my_group)
            bot.send_message(message.chat.id, f'Я нашел группу {my_answers[0]}, кстати, у меня есть {len(os.listdir())} файла/ов')
            print('6', os.getcwd())
            print('7', os.listdir())
            mess = bot.send_message(message.chat.id, 'Какую композицию мне найти?')
            bot.register_next_step_handler(mess, your_song)
        else:
            bot.send_message(message.chat.id, "Группа не найдена, введите снова /find")
            bot.clear_step_handler_by_chat_id(message.chat.id)

    except FileNotFoundError as no_group:
        except_mess = bot.send_message(message.chat.id, "Группа не найдена, введите снова /find")
        bot.clear_step_handler_by_chat_id(message.chat.id)


def your_song(message):
    my_path = os.getcwd()
    my_answers.append(message.text)
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сохранить в коллекцию", callback_data='save')
    markup.add(button1)
    user_info = message.from_user.id
    try:
        my_file = transliter.all_finder(my_path, my_answers[1].lower(), 'song')
        print('8', my_file)
        if my_file != [set()]:
            info.append(my_file)
            info.append(message.from_user.id)
            bot.send_message(message.chat.id, f'Я нашел композицию {my_answers[1]}', reply_markup=markup)
            song_my_file = open(my_file, 'rb')
            bot.send_document(message.chat.id, song_my_file)

        else:
            bot.send_message(message.chat.id, "Песня не найдена, введите снова /find")
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


@bot.message_handler(commands=['start'])
def start(message):

    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_collection = types.KeyboardButton('Открыть коллекцию')
    markup_reply.add(button_collection)
    if message.from_user.username is not None:
        bot.send_message(message.chat.id, f'Добро пожаловать, путник {message.from_user.username}!', reply_markup=markup_reply)
    else:
        bot.send_message(message.chat.id, f'Добро пожаловать, путник!', reply_markup=markup_reply)

    bot.send_message(message.chat.id, 'Чтобы найти музыкальную группу, введите /find\n'
                                      'Также отсюда можешь открыть свою коллекцию файлов\n'
                                      'Можете ввести /send_file для отправки своих файлов и добавления их в коллекцию')


@bot.message_handler(commands=['send_file'])
def send_file(message):
    bot.send_message(message.chat.id, "Присылай свой файл, сохраню в твою коллекцию")


@bot.message_handler(content_types=['document'])
def get_file(message):
    os.chdir(r"C:\Users\steve\Chat-bot-TabsFinderBot")
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    file_name = message.document.file_name
    path = r'C:\Users\steve\Chat-bot-TabsFinderBot\For_Project\Sent_Tabs'
    path_2 = (os.path.join(path, file_name))
    print(path_2)
    with open(path_2, 'wb') as new_file:
        new_file.write(downloaded_file)

    print(message.document.file_id, message.document.file_name)
    func = database_main.add_to_collection_table_from_send(message.from_user.id, message.document.file_name, message.document.file_id, 1)
    print('10', func)
    if func == 'in collection':
        bot.send_message(message.chat.id, f'Файл уже в коллекции {message.from_user.username}')
    else:
        bot.send_message(message.chat.id, f'Файл сохранен в коллекцию {message.from_user.username}')


@bot.message_handler(content_types=['text'])
def text_func(message):
    user_id_start = message.from_user.id
    os.chdir(r"C:\Users\steve\Chat-bot-TabsFinderBot")
    if message.text == 'Открыть коллекцию':
        inline_markup_2 = types.InlineKeyboardMarkup(row_width=2)
        button_open_collection = types.InlineKeyboardButton('Открыть всю коллекцию', callback_data= 'open_collection')
        button_open_file_in_collection = types.InlineKeyboardButton('Открыть файл из коллекции', callback_data= 'open_file')
        inline_markup_2.add(button_open_collection, button_open_file_in_collection)
        AmountOfFiles = database_main.elements_of_collection(user_id_start, "AmountOfFiles")
        bot.send_message(message.chat.id, f'В вашей коллекции {AmountOfFiles} файла/ов', reply_markup= inline_markup_2)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'open_collection':
            print(call.from_user.id)
            my_coll = database_main.elements_of_collection(call.from_user.id, 'ShowAll')
            for val in my_coll:
                bot.send_message(call.message.chat.id, f'`{val}`', parse_mode='MarkDown')
        if call.data == 'open_file':
            mess = bot.send_message(call.message.chat.id, 'Какой файл из коллекции вы хотите скачать?')
            bot.register_next_step_handler(mess, file_open)
        if call.message:
            if call.data == 'save':
                print('9', call.from_user.id)
                print('9.1', info)
                os.chdir(r"C:\Users\steve\Chat-bot-TabsFinderBot")
                func = database_main.add_to_collection_table_from_tabs(call.from_user.id, info[0], info[1], 0)
                print('10', func)
                if func == 'in collection':
                    bot.send_message(call.message.chat.id, f'Файл уже в коллекции {call.from_user.username}')
                else:
                    bot.send_message(call.message.chat.id, f'Файл сохранен в коллекцию {call.from_user.username}')


def file_open(message):
    try:
        os.chdir(r"C:\Users\steve\Chat-bot-TabsFinderBot")
        print('in func')
        file_from_collection_database = message.text
        path_from_tabs_database = database_main.open_file_from_collection(message.from_user.id, file_from_collection_database)
        print('Path_1', path_from_tabs_database)
        os.chdir(path_from_tabs_database)
        print('11', file_from_collection_database)
        print(os.getcwd())
        file_to_open = open(file_from_collection_database, 'rb')
        bot.send_document(message.chat.id, file_to_open)
    except Exception as file_error:
        bot.send_message(message.chat.id, "Файл в коллекции не найден")


try:
    bot.polling(none_stop=True, interval=0)
except Exception as ex:
    print(ex)
