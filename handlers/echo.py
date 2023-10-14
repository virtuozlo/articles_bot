from config.loader import bot
from telebot import types


@bot.message_handler(func=lambda m: True)
def echo_all(message: types.Message):
    bot.reply_to(message, message.text)
