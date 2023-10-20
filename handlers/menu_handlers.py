from config.loader import bot
from keyboards.kb_filters import *
from keyboards.menu_inline_kb import create_buttons_federal_menu, get_button_prev
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
    #  Заменить str на bool
    for i in data:
        if data[i] == 'False':
            data[i] = False
    tmp = [data[i] for i in data if data[i] != 'rules']  # Посчитать false,
    if tmp.count(False) == 2:  # Добавить шаг назад (изменить документ на false)
        data['action'] = False
    elif tmp.count(False) == 1:  # Добавить шаг назад (изменить часть на false)
        data['part'] = False
    elif not tmp.count(False):
        data['article'] = False
    description, keyboard = create_buttons_federal_menu(**{'action': data['action'],
                                                           'part': data['part'],
                                                           'article': data[
                                                               'article']})
    bot.send_message(chat_id, description, parse_mode='HTML',
                     reply_markup=keyboard)
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
    data = for_menu_action.parse(call.data)
    description, keyboard = create_buttons_federal_menu(**{'action': data['action'],
                                                           'part': False,
                                                           'article': False})
    bot.send_message(chat_id, description, parse_mode='HTML',
                     reply_markup=keyboard)
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
    data = for_menu_part.parse(callback_data=call.data)
    description, keyboard = create_buttons_federal_menu(**{'action': data['action'],
                                                           'part': data['part'],
                                                           'article': False})
    bot.send_message(chat_id, description, parse_mode='HTML',
                     reply_markup=keyboard)
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
    data = for_menu_article.parse(callback_data=call.data)
    action, part, article = data['action'], data['part'], data['article']
    answer = ''
    description, keyboard = create_buttons_federal_menu(**{'action': action,
                                                           'part': part,
                                                           'article': False})
    try:
        answer = file_reader(action + '/' + part + '/' + article)
    except FileNotFoundError:
        answer = 'Ошибка нахождения файла, попробуйте заново /start'
    finally:
        if not answer:
            answer = 'Файл пока пуст. Жди и посмотри что-то другое'
        bot.send_message(chat_id, answer, parse_mode='HTML', )
        bot.send_message(chat_id, f'Клик',
                         reply_markup=get_button_prev(action, part, article))
        logger.info(str(action))
        bot.delete_message(chat_id, message_id)
