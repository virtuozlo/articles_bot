import os
from typing import Tuple, Union, List
from telebot.types import Message, CallbackQuery, InputMediaPhoto

from config.logger import logger

PATH_TO_PHOTO = os.path.join(os.getcwd(), 'photo')


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


def get_set_media(path: str) -> List[InputMediaPhoto]:
    """
    :param path: путь до папки с фото
    :return: List[фоточки]
    """
    images = []
    path = os.path.join(PATH_TO_PHOTO, path)
    #  Оставить только фото формат .jpg
    list_photo = [i for i in os.listdir(path) if i.endswith(('.jpg', '.JPG'))]
    for image in list_photo:
        images.append(InputMediaPhoto(
            media=open(path + '/' + image, 'rb')
        ))
    return images


def photo_request(path: str) -> bool:
    """
    Проверить, есть ли в текущей директории фото
    :param path: Текущий путь
    :return: есть / нет фото
    """
    try:
        path_photo = os.listdir(os.path.join(PATH_TO_PHOTO, path))  # Здесь должны быть фото
        return any(i for i in path_photo if i.endswith(('.jpg', '.JPG')))
    except FileNotFoundError as e:
        return False
