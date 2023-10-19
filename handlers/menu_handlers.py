from config.loader import bot
from keyboards.kb_filters import *
from keyboards.menu_inline_kb import create_buttons_federal_menu
from utils.reader_files import file_reader, get_msg
from config.logger import logger
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=None, start_config=for_start.filter())
def go_prev(call: CallbackQuery):
    """
    Функция прорабатывает calldata и решает, какой параметр сделать false, что бы уйти на шаг назад
    :param call:
    :return:
    """
    message, user_id, chat_id, message_id = get_msg(call, True)
    logger.info(' ')
    data = for_start.parse(callback_data=call.data)
    text = 'Выберете документ'
    #  Заменить str на bool
    for i in data:
        if data[i] == 'False':
            data[i] = False
    tmp = [data[i] for i in data if data[i] != 'rules']  # Посчитать false,
    if tmp.count(False) == 2:  # Добавить шаг назад (изменить документ на false)
        data['action'] = False
        text = 'Выберете документ'
    elif tmp.count(False) == 1:  # Добавить шаг назад (изменить часть на false)
        data['part'] = False
        text = 'Выберете главу'
    bot.send_message(chat_id, text, reply_markup=create_buttons_federal_menu(**{'action': data['action'],
                                                                                'part': data['part'],
                                                                                'article': data[
                                                                                    'article']}))
    bot.delete_message(chat_id, message_id)


@bot.callback_query_handler(func=None, start_config=for_menu_action.filter())
def start_federal_menu(call: CallbackQuery):
    """
    Ловит выбор пользователя из стартового меня.
    :param call: Выбор - федеральный кодекс
    :return: Перевод на меня выбора глав
    """
    message, user_id, chat_id, message_id = get_msg(call, True)
    logger.info(' ')
    action = for_menu_action.parse(call.data)
    bot.send_message(chat_id, f'Выберете главу',
                     reply_markup=create_buttons_federal_menu(**{'action': action['action'],
                                                                 'part': False,
                                                                 'article': False}))
    bot.delete_message(chat_id, message_id)


@bot.callback_query_handler(func=None, check_config=for_menu_part.filter())
def get_federal_rules_part(call: CallbackQuery):
    """
    Ловит выбор главы ФЗ
    :param call: Выбор - глава ФЗ
    :return:
    """
    message, user_id, chat_id, message_id = get_msg(call, True)
    logger.info(' ')
    callback_data = for_menu_part.parse(callback_data=call.data)
    bot.send_message(chat_id, f'Выберете Статью',
                     reply_markup=create_buttons_federal_menu(**{'action': callback_data['action'],
                                                                 'part': callback_data['part'],
                                                                 'article': False
                                                                 }))
    bot.delete_message(chat_id, message_id)


@bot.callback_query_handler(func=None,
                            check_config=for_menu_article.filter())
def get_some_article(call: CallbackQuery):
    """
    Вывести статью
    :param call: Все интересующие данные пути до статьи
    :return:
    """
    message, user_id, chat_id, message_id = get_msg(call, True)
    logger.info(' ')
    callback_data = for_menu_article.parse(callback_data=call.data)
    action, part, article = callback_data['action'], callback_data['part'], callback_data['article']
    answer = ''
    try:
        answer = file_reader(action + '/' + part + '/' + article)
    except FileNotFoundError:
        answer = 'Ошибка нахождения файла, попробуйте заново /start'
    finally:
        if not answer:
            answer = 'Файл пока пуст. Жди и посмотри что-то другое'
        bot.send_message(chat_id, answer)
        bot.send_message(chat_id, f'Выберете Статью',
                         reply_markup=create_buttons_federal_menu(**{'action': action,
                                                                     'part': part,
                                                                     'article': False
                                                                     }))
    bot.delete_message(chat_id, message_id)
