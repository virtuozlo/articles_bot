from config.my_config import PATH_TO_FILES


def file_reader(filename: str):
    """

    :param filename:
    :return: генератор строк файла
    """
    with open(PATH_TO_FILES + filename, encoding='utf-8') as f:
        read_data = f.read()
    return read_data

