from config.loader import bot
from config.state_menu import MenuStates
from keyboards import menu_inline_kb
from config.logger import logger
from utils.reader_files import get_msg
from telebot.types import Message


@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    """
    Отправляет пользователя к выбору раздела
    :param message:
    :return:
    """
    message, user_id, chat_id, message_id = get_msg(message)
    logger.info(' ')
    bot.set_state(message.from_user.id, MenuStates.start, message.chat.id)
    bot.send_message(chat_id, 'Выберите раздел',
                     reply_markup=menu_inline_kb.create_buttons_federal_menu(**{'action': False,
                                                                                'part': False,
                                                                                'article': False}))


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    message, user_id, chat_id, message_id = get_msg(message)
    bot.send_message(chat_id, 'Бот тестируется и дополняется')
