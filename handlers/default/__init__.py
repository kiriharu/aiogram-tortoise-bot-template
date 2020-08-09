from aiogram import Dispatcher

from .login import login_test
from .start import start_cmd


def setup(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])
    dp.register_message_handler(login_test, commands=['login'])
