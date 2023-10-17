from typing import List
import os

from config.my_config import PATH_TO_FILES


def file_reader(filename: str):
    """

    :param filename:
    :return: генератор строк файла
    """
    with open(PATH_TO_FILES + filename, encoding='utf-8') as f:
        read_data = f.read()
    return read_data


def directions_list(dir_name: str) -> List:
    """
    Выведет все файлы / папки указанного пути
    :param path:
    :return:
    """
    return os.listdir(PATH_TO_FILES + '/' + dir_name)
#
# print(PATH_TO_FILES)
# print(os.listdir(PATH_TO_FILES + '/' + 'фз57' + '/'+ 'Глава_1'))
