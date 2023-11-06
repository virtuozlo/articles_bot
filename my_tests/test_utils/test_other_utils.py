import os.path
import unittest
from telebot.types import InputMediaPhoto, Message, User, Chat, InlineKeyboardMarkup
from utils.other_utils import get_set_media, get_descr_and_keyboard
from datetime import date
import json


class TestInputMedia(unittest.TestCase):
    def setUp(self):
        self.user_id = 12345
        self.username = 'username'
        # self.photo_set = []
        # self.photo = InputMediaPhoto(media=open((os.path.join(os.getcwd(), 'for_test_photo.jpg')), 'rb'))
        # for _ in range(5):
        #     self.photo_set.append(self.photo)

    def test_get_set_media(self):
        result = get_set_media(os.path.join('Общее', 'Паспорта'))
        self.assertTrue(isinstance(result[0], InputMediaPhoto))

    def test_get_descr_and_keyboard(self):
        descr, kb = get_descr_and_keyboard('', 12345,'name')
        self.assertTrue(isinstance(descr,str))
        self.assertTrue(isinstance(kb, InlineKeyboardMarkup))

