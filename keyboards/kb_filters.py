from config.logger import logger
from telebot import AdvancedCustomFilter, types
from telebot.callback_data import CallbackData, CallbackDataFilter

for_start = CallbackData('path_dir', prefix='path')  # Для выбора части закона
for_photo = CallbackData('path_dir', prefix='path_photo')  # Для вывода фото


class StartActions(AdvancedCustomFilter):
    """
    Разбирает выбор пользователя на команду старт
    """
    logger.info(' ')
    key = 'start_config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)
