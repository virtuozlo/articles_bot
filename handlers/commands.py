from config.loader import bot
from keyboards import reply, inline


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message.chat.id, 'Another Markup', reply_markup=inline.my_inl_keyb)


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    bot.send_message(message.chat.id, 'Вот ваша клава', reply_markup=reply.my_keyb)
