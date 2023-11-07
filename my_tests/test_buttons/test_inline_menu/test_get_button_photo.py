import os.path
import unittest

import keyboards
from keyboards.menu_inline_kb import get_button_photo, get_button_prev, buttons_choose, create_keyboard_menu
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class TestKeyboards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user_id = 123
        cls.username = 'username'
        try:
            os.mkdir(os.path.join(os.getcwd(), 'photo'))
        except FileExistsError:
            pass
        try:
            os.mkdir(os.path.join(os.getcwd(), 'text_files'))
            with open(os.path.join(os.getcwd(), 'text_files', 'description'),'w') as file:
                file.write('test')
        except FileExistsError:
            pass
        os.mkdir(os.path.join(os.getcwd(), 'text_files', 'ex_dir'))
        with open(os.path.join(os.getcwd(), 'text_files', 'ex_dir', 'description'),'w') as file:
            file.write('test')
        with open(os.path.join(os.getcwd(), 'text_files', 'ex_dir', 'example'),'w') as file:
            file.write('test')
        os.mkdir(os.path.join(os.getcwd(), 'photo', 'ex_dir'))
        os.mkdir(os.path.join(os.getcwd(), 'photo', 'ex_dir', 'ex_subdir'))
        with open(os.path.join(os.getcwd(), 'photo', 'ex_dir', 'ex_subdir', 'example.jpg'), 'w') as file:
            file.close()

    @classmethod
    def tearDownClass(cls):
        os.remove(os.path.join(os.getcwd(), 'photo', 'ex_dir', 'ex_subdir', 'example.jpg'))
        os.remove(os.path.join(os.getcwd(), 'text_files', 'ex_dir', 'description'))
        os.remove(os.path.join(os.getcwd(), 'text_files', 'ex_dir', 'example'))
        os.rmdir(os.path.join(os.getcwd(), 'text_files', 'ex_dir'))
        os.rmdir(os.path.join(os.getcwd(), 'photo', 'ex_dir', 'ex_subdir'))
        os.rmdir(os.path.join(os.getcwd(), 'photo', 'ex_dir'))

    def test_get_button_photo(self):
        """
        Проверить возвращение кнопки фото при условии, что фото есть
        :return:
        """

        button = get_button_photo(os.path.join('ex_dir', 'ex_subdir'))
        self.assertTrue(isinstance(button[0], InlineKeyboardButton))

    def test_not_get_button_photo(self):
        """
        Проверить возвращение кнопки фото при условии, что фото нет
        :return:
        """
        button = get_button_photo('false_path')
        self.assertFalse(button)

    def test_get_button_prev(self):
        """
        Поднялись на один вверх
        :return:
        """
        path = get_button_prev(os.path.join('ex_dir', 'ex_subdir'))
        self.assertNotIn('ex_subdir', path[0].text)

    def test_not_prev(self):
        """
        Кнопка не нужна. Возврат false на запрос пустого пути
        :return:
        """
        button = get_button_prev('')
        self.assertFalse(button)

    def test_get_buttons(self):
        """
        Проверить возврат кнопки если задан путь директории
        :return:
        """
        buttons = buttons_choose('')
        self.assertTrue(isinstance(buttons[0], InlineKeyboardButton))

    def test_no_get_buttons(self):
        """
        Проверить возврат None если задан путь к файлу
        :return:
        """
        not_button = buttons_choose(os.path.join('ex_dir', 'ex_subdir', 'example.jpg'))
        self.assertFalse(not_button)

    def test_get_keyboard(self):
        """
        Эпопея всех тестов, что вернётся клавиатура
        :return:
        """
        kb = create_keyboard_menu('')
        self.assertTrue(isinstance(kb, InlineKeyboardMarkup))
