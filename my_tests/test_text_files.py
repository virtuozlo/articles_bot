import os
import unittest
from config.logger import logger
from utils.reader_files import file_reader


class TestFullyFiles(unittest.TestCase):
    """
    Проверка наличия description в каждой папке и подпапке
    Проверка на то, что любой файл для чтения не пуст
    """

    def test_letters_in_files(self, path=os.path.join(os.getcwd(), 'text_files')):
        if os.path.isdir(path):  # Если директория
            for file in [i for i in os.listdir(path) if i != 'description']:
                self.assertIn('description', os.listdir(path))
                description = file_reader(os.path.join(path, 'description'))
                if not description:
                    logger.error(f'Пустой description {path}')
                self.assertTrue(description)
                self.test_letters_in_files(path=os.path.join(path, file))
        else:  # файл
            f = file_reader(path)
            if not f:
                logger.warning(f'ПУстой файл: {path}')
                logger.error(f'Заполнить пустой файл: {path}')
            self.assertTrue(f)
