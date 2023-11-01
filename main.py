from config.loader import bot, bind_filters
from config.set_default_commands import set_default_commands
from config.user_db import UserDb
import handlers


def print_hi(name):  # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    bot.delete_webhook()
    print_hi('PyCharm')
    set_default_commands(bot)
    bind_filters(bot)
    bot.infinity_polling()
