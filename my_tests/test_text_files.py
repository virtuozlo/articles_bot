import os
import unittest
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
                self.test_letters_in_files(path=os.path.join(path, file))
        else:  # файл
            f = file_reader(path)
            self.assertTrue(f)
