import os
from typing import Tuple, Union, List
from telebot.types import Message, CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup
from utils.reader_files import directions_list
from keyboards.menu_inline_kb import create_keyboard_menu

PATH_TO_PHOTO = os.path.join(os.getcwd(), 'photo')


def get_descr_and_keyboard(path: str, user_id: int, nickname: str) -> Tuple[str, InlineKeyboardMarkup]:
    """
    :param nickname: user_name
    :param user_id: user_id
    :param path: Текущая директория
    :return: tuple[str, InlineKeyboard]
    """
    description = directions_list(path, user_id, nickname)  # Взять оттуда description
    keyboard = create_keyboard_menu(path)
    return description, keyboard


def get_set_media(path: str) -> List[InputMediaPhoto]:
    """
    Список фоток для выгрузки тлг
    :param path: путь до папки с фото
    :return: List[фоточки]
    """
    images = []
    path = os.path.join(PATH_TO_PHOTO, path)
    #  Оставить только фото формат .jpg
    list_photo = [i for i in os.listdir(path) if i.endswith(('.jpg', '.JPG'))]
    for image in list_photo:
        images.append(InputMediaPhoto(
            media=open(os.path.join(path, image), 'rb')
        ))
    return images
