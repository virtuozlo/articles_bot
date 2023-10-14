from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton

button = [KeyboardButton('button'), ]
my_keyb = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
my_keyb.add(*button)

