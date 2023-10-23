from config.loader import bot
from config.logger import logger
from keyboards.menu_inline_kb import create_buttons_federal_menu
from utils.other_utils import get_msg
from telebot.types import Message


@bot.message_handler(commands=['start'])
def send_welcome(message: Message) -> None:
    """
    Отправляет в фабрику кнопок path в виде '/', что означает выбрать первую директорию
    :param message:
    """
    message, user_id, chat_id, message_id = get_msg(message)
    logger.info(f'{user_id}')
    description, keyboard = create_buttons_federal_menu('/')
    bot.send_message(chat_id, description, parse_mode='HTML',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    message, user_id, chat_id, message_id = get_msg(message)
    bot.send_message(chat_id, 'Бот тестируется и дополняется')
