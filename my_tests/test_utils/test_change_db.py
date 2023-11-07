import unittest
import psycopg2
from utils.change_db import change_db
from config.user_db import UserDb


class TestChangeDB(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db = UserDb()
        cls.user_id = 123
        cls.username = 'username'

    @classmethod
    def tearDownClass(cls):
        db = UserDb()
        with db.connection as conn:
            with conn.cursor() as cur:
                return cur.execute("""
                DELETE FROM users WHERE user_id = 123
                """)

    def test_add_change_db(self):
        """
        Работоспособность функции добавления пользователя
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
