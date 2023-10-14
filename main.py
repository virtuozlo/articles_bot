from config.loader import bot
from config.set_default_commands import set_default_commands
import handlers


def print_hi(name):  # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    set_default_commands(bot)
    bot.infinity_polling()
