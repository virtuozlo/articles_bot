from typing import Optional
import psycopg2
from configparser import ConfigParser


class UserDb:
    def __init__(self):
        self.connection = self.conn()

    def config(self, filename='database.ini', section='postgresql'):
        """
        Создать парсер файла - настройки даты базы
        :param filename: initial DB
        :param section: attr DB
        :return: db
        """
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(filename)
        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def conn(self):
        try:
            params = self.config()
            conn = psycopg2.connect(**params)
            return conn
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_table(self):
        command = """
            CREATE TABLE IF NOT EXISTS users (
                        id serial PRIMARY KEY,
                        user_name char(20),
                        user_id integer UNIQUE,
                        user_count integer DEFAULT 1)
            """
        with self.connection as conn:
            with conn.cursor() as cur:
                return cur.execute(command)

    def add_user(self, user_id: int, user_name: Optional[str] = None):
        """
        Добавить пользователя по id
        Добавит ник, если есть
        :param user_id: id user
        :param user_name: nickname
        :return:
        """
        with self.connection as conn:
            with conn.cursor() as cur:
                return cur.execute("INSERT INTO users(user_name, user_id) VALUES (%s,%s) ", (user_name, user_id))

    def update_user(self, user_id: int, user_name: str):
        """

        :param user_id: user_id
        :param user_name: next user_name
        :return: update db
        """
        with self.connection as conn:
            with conn.cursor() as cur:
                return cur.execute("""
            UPDATE users
            SET user_name = %s,
                user_count = user_count + 1
            WHERE user_id = %s
            """, (user_name, user_id,))

    def get_user(self, id_user: int):
        """
        вернёт список со строкой пользователя
        fetchone - попнет один результат
        fetchall - выведет все результаты
        fetchmany  хз в чем разница. Первый результат даст
        :return:
        """
        with self.connection as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, user_name FROM users WHERE user_id = %s", (id_user,))
                return cur.fetchone()


# if __name__ == '__main__':
#     db = UserDb()
#     print(db.connection)
#     db.create_table()
    #  Examples
    #  db.get_user(user_id) - Выдаст список совпадений (использовать всегда, что бы убедиться что пользователь есть/нет)
    # db.add_user(123124, 'user_name') #- Добавить пользователя, если имени нет, то не беда. Ошибки не будет
    #  db.update_user(user_id, user_name) - Изменит name