from aiogram import Dispatcher
from .start import start_cmd
from .login import login_test


def setup(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])
    dp.register_message_handler(login_test, commands=['login'])