import os.path
from typing import Tuple, List, Optional
from utils.reader_files import PATH_TO_FILES
import telebot.types
from config.logger import logger
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .kb_filters import for_start, for_photo
from utils.reader_files import directions_list


def get_button_photo(path: str) -> List[InlineKeyboardButton]:
    """
    Создать кнопку получения фото с CallBackData для фото
    :param path:
    :return:
    """
    return [InlineKeyboardButton('Загрузить фото', callback_data=for_photo.new(path_dir=path))]


def get_button_prev(path: str) -> Optional[List[telebot.types.InlineKeyboardButton]]:
    """
    Делает из path - list. Если он не пуст, то pop последний аргумент и снова сделать строку
    Даже если список пуст, вернёт '/'
    :param path: Текущий путь
    :param message_id: id сообщения с фото. Отправлен кнопкой "назад" из callback с фото
    :return: preview button
    """
    print(f'Принимает на вход для кнопки назад {path}')
    if path:
        path = path.split('\\')
        if path[:len(path)-1]:  # Если осталось куда идти назад
            path = os.path.join(*path[:len(path)-1])
        else:
            path = ''
        logger.info(f'Получение информации, что путь есть {path}')
        return [InlineKeyboardButton('Назад', callback_data=for_start.new(path_dir=path))]
    else:
        logger.info(f'Нет пути назад')
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
            path_dir = os.path.join(path, button)
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
    description, buttons = buttons_choose(path)  # Вернет desr - Общая информация для кнопок либо текст из файла
    prev_button = get_button_prev(path)  # Кнопка "назад" В той функции решает нужна она или нет и какая будет
    keyboard.add(*buttons)
    if prev_button:  # Если есть необходимость
        keyboard.add(*prev_button)  # то добавить
    return description, keyboard
