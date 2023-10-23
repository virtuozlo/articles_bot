from config.loader import bot
from keyboards.kb_filters import *
from keyboards.menu_inline_kb import create_buttons_federal_menu
from utils.other_utils import get_msg
from config.logger import logger
from telebot.types import CallbackQuery


@bot.callback_query_handler(func=None, start_config=for_start.filter())
def reading_menu(call: CallbackQuery) -> None:
    """
    Разбирает call на id всего, что только можно (что бы вызывать один раз)
    Отправляет в фабрику кнопок path из callback data
    description - Файл в директории с описанием директории, либо текст из файла (endpoint директории)
    keyboard - Кнопки, где их названия - названия файлов в директории, либо только кнопка "назад"
    :param call:
    """
    message, user_id, chat_id, message_id = get_msg(call, True)
    my_data = for_start.parse(callback_data=call.data)
    print(my_data)
    logger.info(' ')
    description, keyboard = create_buttons_federal_menu(my_data['path_dir'])
    bot.send_message(chat_id, description, parse_mode='HTML',
                     reply_markup=keyboard)
    bot.delete_message(chat_id, message_id)
