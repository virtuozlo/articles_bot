from config.loader import bot, db_user
from config.state_menu import MenuStates
from keyboards import menu_inline_kb
from config.logger import logger


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Отправляет пользователя к выбору раздела
    :param message:
    :return:
    """
    logger.info(' ')
    if not db_user.check_user(message.from_user.id):
        db_user.add_user(message.from_user.id)
        logger.error(f'user_id: {message.from_user.id}')
    bot.set_state(message.from_user.id, MenuStates.start, message.chat.id)
    bot.send_message(message.chat.id, 'Выберите раздел',
                     reply_markup=menu_inline_kb.create_buttons_federal_menu(**{'action': False,
                                                                                'part': False,
                                                                                'article': False}))


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    bot.send_message(message.chat.id, 'Бот тестируется и дополняется')
