"""
Подгрузка основных настроек. Бот, БД и пр
"""
import telebot
from telebot import custom_filters
import os
import psycopg2
from config.user_db import UserDb
from config.logger import logger
from keyboards.kb_filters import StartActions

bot = telebot.TeleBot(os.getenv('MY_TOKEN'), parse_mode=None)


def get_db():
    """
    Попытка установить связь с базой данных
    :return:
    """
    logger.info('Trying get_db')
    try:
        db = UserDb()
        db.create_table()
        logger.info('get_db successfully')
        return db
    except psycopg2.Error as e:
        logger.error(f'Not db connect.\n{e}')
        return 'Not db connect'
    except Exception as e:
        return f'another exception.\n{e}'


db = get_db()


def bind_filters(bot: telebot.TeleBot):
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(StartActions())
