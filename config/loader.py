"""
Подгрузка основных настроек. Бот, БД и пр
"""
import telebot
from telebot import custom_filters

from keyboards.kb_filters import StartActions, AnyActions
from . import my_config

bot = telebot.TeleBot(my_config.MY_TOKEN, parse_mode=None)


def bind_filters(bot: telebot.TeleBot):
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(StartActions())
    bot.add_custom_filter(AnyActions())
