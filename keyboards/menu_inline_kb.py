from typing import Tuple, List, Optional

import telebot.types
from config.logger import logger
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .kb_filters import for_start
from utils.reader_files import directions_list


def get_button_prev(path: str) -> Optional[List[telebot.types.InlineKeyboardButton]]:
    """
    Делает из path - list. Если он не пуст, то pop последний аргумент и снова сделать строку
    Даже если список пуст, вернёт '/'
    :return: preview button
    """
    path = [i for i in path.split('/') if i]
    if path:
        path.pop()
        return [InlineKeyboardButton('Назад', callback_data=for_start.new(path_dir='/'.join(path) + '/'))]
    else:
        return None


def buttons_choose(path: str) -> Tuple[str, List[InlineKeyboardButton]]:
    """
    Разбирает path, который состоит из списка с названиями папок
    :param path: Список файлов (вложенных и текущего)
    :return: list of buttons
    """
    logger.info(' ')
    description, folder = directions_list(path)
    buttons = []
    if folder:  # Если была директория
        for button in folder:
            path_dir = (path + button + '/')
            buttons.append(
                InlineKeyboardButton(button, callback_data=for_start.new(path_dir=path_dir))
            )
    return description, buttons


def create_buttons_federal_menu(path) -> Tuple[str, telebot.types.InlineKeyboardMarkup]:
    """
    Создать кнопки для команды ФЗ
    """
    logger.info(' ')
    keyboard = InlineKeyboardMarkup()
    description, buttons = buttons_choose(path)
    prev_button = get_button_prev(path)
    keyboard.add(*buttons)
    if prev_button:
        keyboard.add(*prev_button)
    return description, keyboard
