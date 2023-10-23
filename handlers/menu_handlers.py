from config.loader import bot
from keyboards.kb_filters import *
from keyboards.menu_inline_kb import create_buttons_federal_menu, get_button_photo, get_button_prev
from utils.other_utils import get_msg, photo_request, get_set_media
from config.logger import logger
from telebot.types import CallbackQuery, InlineKeyboardMarkup, InputMediaPhoto


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
    logger.info(' ')
    description, keyboard = create_buttons_federal_menu(my_data['path_dir'])
    get_photo_request = photo_request(my_data['path_dir'])
    if get_photo_request:  # Здесь будет делаться кнопка дай фото
        keyboard.add(*get_button_photo(my_data['path_dir']))
    bot.send_message(chat_id, description, parse_mode='HTML',
                     reply_markup=keyboard)
    bot.delete_message(chat_id, message_id)


@bot.callback_query_handler(func=None, start_config=for_photo.filter())
def get_photo(call: CallbackQuery) -> None:
    print(call.message.id)
    my_data = for_photo.parse(callback_data=call.data)
    photos = get_set_media(my_data['path_dir'])  # Возврат списка с tlg-фото
    keyboard = InlineKeyboardMarkup()
    keyboard.add(*get_button_prev(my_data['path_dir']))
    bot.send_media_group(call.message.chat.id,
                         media=photos, protect_content=True)
    bot.send_message(call.message.chat.id, 'Предыдущий шаг', reply_markup=keyboard)
    bot.delete_message(call.message.chat.id, call.message.id)
