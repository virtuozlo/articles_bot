import os.path
import unittest
from telebot.types import InputMediaPhoto, Message, User, Chat, InlineKeyboardMarkup
from utils.other_utils import get_set_media, get_descr_and_keyboard
from datetime import date
import json


class TestInputMedia(unittest.TestCase):
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

    def test_get_set_media(self):
        result = get_set_media(os.path.join('ex_dir', 'ex_subdir'))
        self.assertTrue(isinstance(result[0], InputMediaPhoto))

    def test_get_descr_and_keyboard(self):
        descr, kb = get_descr_and_keyboard('', self.user_id, self.username)
        self.assertTrue(isinstance(descr, str))
        self.assertTrue(isinstance(kb, InlineKeyboardMarkup))
