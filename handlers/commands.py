from config.loader import bot
from config.logger import logger
from utils.other_utils import get_descr_and_keyboard
from telebot.types import Message


@bot.message_handler(commands=['start'])
def send_welcome(message: Message) -> None:
    """
    Отправляет в фабрику кнопок path в виде '/', что означает выбрать первую директорию
    :param message:
    """
    logger.info(f'{message.from_user.id} в меню')
    description, keyboard = get_descr_and_keyboard('', message)
    bot.send_message(message.chat.id, description, parse_mode='HTML',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    bot.send_message(message.chat.id, 'Бот тестируется и дополняется')
