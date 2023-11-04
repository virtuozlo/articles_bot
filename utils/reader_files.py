import os
from config.logger import logger
from utils.change_db import change_db

PATH_TO_FILES = os.path.join(os.getcwd(), 'text_files')


def file_reader(filename: str) -> str:
    """

    :param filename:
    :return: строки файла
    """
    logger.info(' ')
    read_data = ''
    try:
        with open(os.path.join(PATH_TO_FILES, filename), encoding='utf-8') as f:
            read_data = f.read()
    except Exception as e:
        logger.error(e)
        read_data = 'Ошибка чтения файла'
    finally:
        return read_data


def directions_list(dir_name: str, user_id: int, nickname: str) -> str:
    """
    Выведет все файлы / папки указанного пути
    :param nickname: Ник
    :param user_id: id
    :param dir_name: Путь к директории
    :return:
    """
    logger.info(' ')
    #  Это для папок
    if os.path.isdir(os.path.join(PATH_TO_FILES, dir_name)):
        description = file_reader(os.path.join(dir_name, 'description'))  # Описание директории
    #  Иначе это файл
    else:
        description = file_reader(dir_name)  # Данные из файла статьи
        change_db(user_id, nickname)  # Добавить к юзеру счётчик выгрузки фото
    return description
