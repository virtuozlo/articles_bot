from config.loader import bot
from config.state_menu import MenuStates
from keyboards import menu_inline_kb


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """
    Отправляет пользователя к выбору раздела
    :param message:
    :return:
    """
    bot.set_state(message.from_user.id, MenuStates.start, message.chat.id)
    bot.send_message(message.chat.id, 'Выберите раздел',
                     reply_markup=menu_inline_kb.create_buttons_federal_menu(**{'action': False,
                                                                                'part': False,
                                                                                'article': False}))


@bot.message_handler(commands=['help'])
def send_keyboard(message):
    bot.send_message(message.chat.id, 'Бот тестируется и дополняется')
