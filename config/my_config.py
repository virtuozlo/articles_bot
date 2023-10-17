from dotenv import load_dotenv, find_dotenv
from .logger import logger
MY_COMMANDS = (
    ('start', 'Запустить бота'),
    ('help', 'Помощь')
)

if not find_dotenv():
    logger.error()
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    logger.info(f'{logger.name}')
    load_dotenv()
