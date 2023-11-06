import os.path

from config.loader import bot
from keyboards.kb_filters import *
from keyboards.menu_inline_kb import create_keyboard_menu, get_button_photo, get_button_prev
from utils.other_utils import get_set_media, get_descr_and_keyboard
from config.logger import logger
from telebot.types import CallbackQuery, InlineKeyboardMarkup


@bot.callback_query_handler(func=None, start_config=for_start.filter())
def reading_menu(call: CallbackQuery) -> None:
    """
    Разбирает call на id всего, что только можно (что бы вызывать один раз)
    Отправляет в фабрику кнопок path из callback data
    description - Файл в директории с описанием директории, либо текст из файла (endpoint директории)
    keyboard - Кнопки, где их названия - названия файлов в директории, либо только кнопка "назад"
    :param call:
    """
    my_data = for_start.parse(callback_data=call.data)
    logger.info(f'{call.message.from_user.id} колупается в меню')
    description, keyboard = get_descr_and_keyboard(my_data['path_dir'], call.from_user.id,call.from_user.username)
    bot.send_message(call.message.chat.id, description, parse_mode='HTML',
                     reply_markup=keyboard)
    bot.delete_message(call.message.chat.id, call.message.id)


@bot.callback_query_handler(func=None, start_config=for_photo.filter())
def get_photo(call: CallbackQuery) -> None:
    logger.info(f'{call.message.from_user.id} выгружает фото')
    my_data = for_photo.parse(callback_data=call.data)
    photos = get_set_media(my_data['path_dir'])  # Возврат списка с tlg-фото
    text = my_data['path_dir'].split('\\')[-1]  # Текущий файл с фото
    description, keyboard = get_descr_and_keyboard(my_data['path_dir'], call.from_user.id,call.from_user.username)
    bot.send_media_group(call.message.chat.id,
                         media=photos, protect_content=True)
    bot.send_message(call.message.chat.id, text, reply_markup=keyboard)
    bot.delete_message(call.message.chat.id, call.message.id)
