import telebot.types
from config.logger import logger
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .kb_filters import for_menu_action, for_menu_article, for_menu_part, for_start
from utils.reader_files import directions_list


def buttons_choose(action, part, article, **kwargs):
    """
    Проходится по каждому данному параметру. Собирает path для функции, которая дает файлы в этом path
    Так же параллельно принимает решение какой CallBackData будет пользоваться
    :param article: Статья части документы
    :param part: Часть документа
    :param action: Выбор пользователя Документ
    :param kwargs: Будет принимать action, part and article и думать какую callbackData вызывать
    :return: list of buttons
    """
    logger.info(' ')
    path = '/'
    factory = for_menu_action
    if action:
        path += action
        factory = for_menu_part
    if part:
        path += '/' + part
        factory = for_menu_article
    if article:
        factory = for_menu_article
        path += '/' + article
    folder = directions_list(path)
    buttons = []
    for button in folder:
        # Если первое вхождение (всё пустое), то присвоить
        # action_button(то, что пойдет в callback кнопкам) название файла директории, иначе оставить отправленное
        action_button = button if not any((action, part, article)) else action
        part_button = button if not (action and part) else part
        article_button = button if (action and part and (not article)) else article
        buttons.append(
            InlineKeyboardButton(button, callback_data=factory.new(action=action_button,
                                                                   part=part_button,
                                                                   article=article_button))
        )
    buttons.append(
        InlineKeyboardButton('Назад', callback_data=for_start.new(action=action,
                                                                  part=part,
                                                                  article=article)))
    return buttons


def create_buttons_federal_menu(**kwargs) -> telebot.types.InlineKeyboardMarkup:
    """
    Создать кнопки для команды ФЗ
    """
    logger.info(' ')
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = buttons_choose(kwargs['action'], kwargs['part'], kwargs['article'])
    keyboard.add(*buttons)
    return keyboard
