import telebot
from telebot.types import BotCommand
from .my_config import MY_COMMANDS


def set_default_commands(bot: telebot) -> None:
    """
    Команды бота
    """
    try:
        bot.set_my_commands(
            [BotCommand(*i) for i in MY_COMMANDS]
        )
    except BaseException as e:
        print(e)