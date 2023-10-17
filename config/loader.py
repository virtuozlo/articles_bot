"""
Подгрузка основных настроек. Бот, БД и пр
"""
import telebot
from telebot import custom_filters
import os
from keyboards.kb_filters import StartActions, AnyActions
from . import my_config
from .user_db import UserDb

bot = telebot.TeleBot(os.getenv('MY_TOKEN'), parse_mode=None)

db_user = UserDb('user.db')


def bind_filters(bot: telebot.TeleBot):
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(StartActions())
    bot.add_custom_filter(AnyActions())
