"""
Подгрузка основных настроек. Бот, БД и пр
"""
import telebot
from telebot import custom_filters
import os
from keyboards.kb_filters import StartActions

bot = telebot.TeleBot(os.getenv('MY_TOKEN'), parse_mode=None)


def bind_filters(bot: telebot.TeleBot):
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.add_custom_filter(StartActions())
