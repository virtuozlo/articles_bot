from typing import Tuple, Union
from telebot.types import Message, CallbackQuery

from config.logger import logger


def get_msg(msg: Union[Message, CallbackQuery], call: bool = False) -> Union[Tuple[Message, int, int, int], str]:
    """
    Функция примет request(msg \ call)
    Вернёт msg / id_user и прочее
    :param msg:
    :param call:
    :return:
    """
    try:
        msg = msg.message if call else msg
    except Exception as e:
        logger.error(e)
    user_id = msg.from_user.id
    chat_id = msg.chat.id
    message_id = msg.id
    return msg, user_id, chat_id, message_id
