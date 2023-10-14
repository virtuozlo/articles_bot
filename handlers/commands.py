from config.loader import bot
from keyboards import reply, inline
from utils.reader_files import file_reader

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    bot.send_message(message.chat.id, 'Another Markup', reply_markup=inline.my_inl_keyb)


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    text = file_reader('second.txt')
    bot.send_message(message.chat.id, text)
