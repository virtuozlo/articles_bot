from .loader import bot
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup

from telebot.storage import StateMemoryStorage

state_storage = StateMemoryStorage()


class MenuStates(StatesGroup):
    """
    State класс для команды history
    """
    start = State()
    federal_rules = State()
    federal_rules_part = State()
    federal_rules_get_article = State()
    criminal_rules = State()
    third = State()
