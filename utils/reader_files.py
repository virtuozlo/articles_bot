from typing import List, Tuple, Union, Optional
from telebot.types import Message, CallbackQuery
import os
from config.logger import logger


def file_reader(filename: str) -> str:
    """

    :param filename:
    :return: строки файла
    """
    logger.info(' ')
    read_data = ''
    try:
        with open(os.getenv('PATH_TO_FILES') + filename, encoding='utf-8') as f:
            read_data = f.read()
    except Exception as e:
        logger.error(e)
        read_data = 'Ошибка чтения файла'
    finally:
        return read_data


def directions_list(dir_name: str) -> Tuple[str, Optional[List[str]]]:
    """
    Выведет все файлы / папки указанного пути
    :param dir_name: Путь к директории
    :return:
    """
    logger.info(' ')
    dir_name = dir_name[:len(dir_name)-1]  # Убрать последний '/' для чтения файла
    #  Это для папок
    if os.path.isdir(os.getenv("PATH_TO_FILES") + dir_name):
        tmp_dir_lst = os.listdir(f'{os.getenv("PATH_TO_FILES") + dir_name}')  # Все файлы директории
        dir_lst = [i for i in tmp_dir_lst if i != 'description']
        description = [i for i in tmp_dir_lst if i == 'description']
        description = file_reader(dir_name + '/' + description[0])
    #  Иначе это файл
    else:
        description = file_reader(dir_name)
        dir_lst = None
    return description, dir_lst
