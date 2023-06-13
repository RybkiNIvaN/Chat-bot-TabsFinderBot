import telebot
from telebot import types
from telegram_bot_pagination import InlineKeyboardPaginator
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())
bot = telebot.TeleBot(os.getenv('TOKEN'))


def start(message, song_list, page=1, prev_message=None):

    markup = types.InlineKeyboardMarkup()
    left = page - 1 if page != 1 else len(song_list)
    right = page + 1 if page != len(song_list) else 1

    left_button = types.InlineKeyboardButton("←",
                                             callback_data=f'to {left}'
                                             )
    page_button = types.InlineKeyboardButton(f'{str(page)}/{str(len(song_list))}',
                                             callback_data='_'
                                             )

    save_button = types.InlineKeyboardButton("Сохранить в коллекцию",
                                             callback_data='save'
                                             )
    right_button = types.InlineKeyboardButton("→",
                                              callback_data=f'to {right}'
                                              )
    markup.add(page_button)
    markup.add(left_button, right_button)
    markup.add(save_button)
    #print('pagination NOT OK', message)
    #bot.send_message(message, "Здесь будет пагинация", reply_markup=markup)
    #print('pagination OK')
    try:
        print(song_list[page-1], message.chat.id)
        current_file = song_list[page-1]
        song_my_file = open(song_list[page-1], 'rb')
        bot.send_document(message.chat.id,
                          document=song_my_file,
                          caption=str(page),
                          reply_markup=markup
                          )

    except Exception as ex:
        bot.send_message(message.chat.id,
                         song_list[page-1],
                         reply_markup=markup
                         )
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    try:
        bot.delete_message(message.chat.id,
                           prev_message.id
                           )

    except:
        pass


def coll_pages(message, song_list, page=1):
    paginator = InlineKeyboardPaginator(
        len(song_list),
        current_page=page,
        data_pattern='song#{page}'
    )
    bot.send_message(
        message.chat.id,
        song_list[page-1],
        reply_markup=paginator.markup
    )



