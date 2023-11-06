import os
import unittest
from utils.reader_files import directions_list
import utils.reader_files


class TestReaderUtils(unittest.TestCase):
    def setUp(self):
        self.filename = 'file_for_test'
        self.base_dir_name = os.getcwd()
        self.username = 'username'
        self.user_id = 123
        utils.reader_files.PATH_TO_FILES = os.path.join(self.base_dir_name, 'my_tests', 'test_utils')

    def test_check_description(self):
        """
        Если забыл включить description в директорию
        :return:
        """
        directions_list('', self.user_id, self.username)
        self.assertRaises(FileNotFoundError)

    def test_check_description_not_empty(self):
        """
        Если забыл написать в описании директории хоть что-то
        :return:
        """
        description = directions_list('', self.user_id, self.username)
        self.assertTrue(description)

    def test_get_article(self):
        """
        Проверка чтения файла. Не может быть пустым
        :return:
        """
        article = directions_list('file_for_test', self.user_id, self.username)
        self.assertTrue(article)

