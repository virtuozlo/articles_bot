import os.path
import unittest

import keyboards
from keyboards.menu_inline_kb import get_button_photo, get_button_prev, buttons_choose, create_keyboard_menu
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class TestKeyboards(unittest.TestCase):
    def test_get_button_photo(self):
        """
        Проверить возвращение кнопки фото при условии, что фото есть
        :return:
        """

        button = get_button_photo(os.path.join('Медицина'))
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
        path = get_button_prev(os.path.join('Медицина', 'Аптечки'))
        self.assertNotIn('Аптечки', path[0].text)

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
        not_button = buttons_choose(os.path.join('text_files', 'Медицина', 'description'))
        self.assertFalse(not_button)

    def test_get_keyboard(self):
        """
        Эпопея всех тестов, что вернётся клавиатура
        :return:
        """
        kb = create_keyboard_menu('')
        self.assertTrue(isinstance(kb, InlineKeyboardMarkup))
