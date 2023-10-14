from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_button = [InlineKeyboardButton('text', callback_data='yes')]
my_inl_keyb = InlineKeyboardMarkup()
my_inl_keyb.add(*inline_button)