from typing import List
import os
from config.logger import logger


def file_reader(filename: str):
    """

    :param filename:
    :return: генератор строк файла
    """
    logger.info(' ')
    with open(os.getenv('PATH_TO_FILES') + filename, encoding='utf-8') as f:
        read_data = f.read()
    return read_data


def directions_list(dir_name: str) -> List:
    """
    Выведет все файлы / папки указанного пути
    :param dir_name: Путь к директории
    :return:
    """
    logger.info(' ')
    return os.listdir(f'{os.getenv("PATH_TO_FILES") + dir_name}')
