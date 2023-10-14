"""
Подгрузка основных настроек. Бот, БД и пр
"""
import telebot
from . import my_config

bot = telebot.TeleBot(my_config.MY_TOKEN, parse_mode=None)
