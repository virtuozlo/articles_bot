from config.logger import logger
from telebot import AdvancedCustomFilter, types
from telebot.callback_data import CallbackData, CallbackDataFilter

for_menu_action = CallbackData('action', 'part', 'article', prefix='action')
for_menu_part = CallbackData('action', 'part', 'article', prefix='part')
for_menu_article = CallbackData('action', 'part', 'article', prefix='article')  # До выбора части
for_start = CallbackData('action', 'part', 'article', prefix='rules')  # Для выбора части закона


class AnyActions(AdvancedCustomFilter):
    """
    Разбирает любой call кнопок при заданном фильтре
    """
    logger.info(' ')
    key = 'check_config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


class StartActions(AdvancedCustomFilter):
    """
    Разбирает выбор пользователя на команду старт
    """
    logger.info(' ')
    key = 'start_config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)
