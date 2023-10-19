from typing import List, Tuple, Union
from telebot.types import Message, CallbackQuery
import os
from config.logger import logger


def get_msg(msg: Union[Message, CallbackQuery], call: bool = False) -> Tuple[Message, int, int, int]:
    """
    Функция примет request(msg \ call)
    Вернёт msg / id_user и прочее
    :param msg:
    :param call:
    :return:
    """
    msg = msg.message if call else msg
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    message_id = msg.id
    return msg, user_id, chat_id, message_id


def file_reader(filename: str):
    """

    :param filename:
    :return: генератор строк файла
    """
    logger.info(' ')
    with open(os.getenv('PATH_TO_FILES') + filename, encoding='utf-8') as f:
        read_data = f.read()
    return read_data


def directions_list(dir_name: str) -> Tuple:
    """
    Выведет все файлы / папки указанного пути
    :param dir_name: Путь к директории
    :return:
    """
    logger.info(' ')
    tmp_dir_lst = os.listdir(f'{os.getenv("PATH_TO_FILES") + dir_name}')  # Все файлы директории
    dir_lst = [i for i in tmp_dir_lst if i != 'description']
    description = [i for i in tmp_dir_lst if i == 'description']
    description = file_reader(dir_name + '/' + description[0])
    return description, dir_lst
