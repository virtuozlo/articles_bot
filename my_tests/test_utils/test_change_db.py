import unittest
import psycopg2
from utils.change_db import change_db
from config.user_db import UserDb


class TestChangeDB(unittest.TestCase):
    def setUp(self):
        self.db = UserDb()
        self.user_id = 123
        self.username = 'username'

    def test_add_change_db(self):
        """
        Работоспособность функции добавления пользвателя
        :return:
        """
        change_db(self.user_id, self.username)
        self.assertTrue(self.db.get_user(id_user=self.user_id))

    def test_edit_change_ds(self):
        """
        Работоспособность изменения ника. Второй элемент в get_user
        :return:
        """
        change_db(self.user_id, 'another_nickname')
        self.assertIn('another_nickname', self.db.get_user(id_user=self.user_id)[1])
