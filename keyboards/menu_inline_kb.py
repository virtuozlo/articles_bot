import os.path
from typing import List, Optional
import telebot.types
from config.logger import logger
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .kb_filters import for_start, for_photo

PATH_TO_FILES = os.path.join(os.getcwd(), 'text_files')
PATH_TO_PHOTO = os.path.join(os.getcwd(), 'photo')


def get_button_photo(path: str) -> Optional[List[InlineKeyboardButton]]:
    """
    Создать кнопку получения фото с CallBackData для фото
    :param path:
    :return:
    """
    logger.info(f'{path}')
    try:
        path_photo = os.listdir(os.path.join(PATH_TO_PHOTO, path))  # Здесь должны быть фото
        if any(i for i in path_photo if i.endswith(('.jpg', '.JPG'))):
            return [InlineKeyboardButton('Загрузить фото', callback_data=for_photo.new(path_dir=path))]
    except FileNotFoundError as e:
        return None
    except OSError as e:  # Значит идёт выгрузка фото
        return None


def get_button_prev(path: str) -> Optional[List[telebot.types.InlineKeyboardButton]]:
    """
    Делает из path - list. Если он не пуст, то pop последний аргумент и снова сделать строку
    Даже если список пуст, вернёт '/'
    :param path: Текущий путь
    :param message_id: id сообщения с фото. Отправлен кнопкой "назад" из callback с фото
    :return: preview button
    """
    if path:
        path = path.split('\\')
        if path[:len(path) - 1]:  # Если осталось куда идти назад
            text = path[:len(path) - 1][-1]
            path = os.path.join(*path[:len(path) - 1])
        else:
            path = ''
            text = 'в меню'
        logger.info(f' ')
        return [InlineKeyboardButton(f'Назад --> {text}', callback_data=for_start.new(path_dir=path))]
    else:
        logger.info(f' ')
        return None


def buttons_choose(path: str) -> Optional[List[InlineKeyboardButton]]:
    """
    :param path: Текущий путь
    :return: list of buttons
    """
    print(PATH_TO_FILES)
    logger.info(' ')
    buttons = []
    if os.path.isdir(os.path.join(PATH_TO_FILES, path)):  # Если это директория
        folder = os.listdir(os.path.join(PATH_TO_FILES, path))
        folder = [i for i in folder if i != 'description']  # то убрать description
        for button in folder:
            path_dir = os.path.join(path, button)
            buttons.append(
                InlineKeyboardButton(button, callback_data=for_start.new(path_dir=path_dir))
            )
        return buttons
    return None  # Если это файл


def create_keyboard_menu(path) -> telebot.types.InlineKeyboardMarkup:
    """
    Создать кнопки для команды ФЗ
    """
    logger.info(' ')
    keyboard = InlineKeyboardMarkup()
    buttons = buttons_choose(path)  # Вернет кнопки, если это директория
    if buttons:
        keyboard.add(*buttons)
    if get_button_photo(path):
        keyboard.add(*get_button_photo(path))
    prev_button = get_button_prev(path)  # Кнопка "назад" В той функции решает нужна она или нет и какая будет
    if prev_button:  # Если есть необходимость
        keyboard.add(*prev_button)  # то добавить
    return keyboard
