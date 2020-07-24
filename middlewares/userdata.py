from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.handler import current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from models.user import User


def userdata_required(f):
    """Setting login_required to function"""
    setattr(f, 'userdata_required', True)
    return f


class UserMiddleware(BaseMiddleware):

    def __init__(self):
        super(UserMiddleware, self).__init__()

    async def get_userdata(self, telegram_id: int) -> User:
        handler = current_handler.get()
        if handler:
            attr = getattr(handler, 'userdata_required', False)
            if attr:
                # Setting user
                user, _ = await User.get_or_create(telegram_id=telegram_id)
                return user

    async def on_process_message(self, message: Message, data: dict):
        data['user'] = await self.get_userdata(message.from_user.id)

    async def on_process_callback_query(self, callback_query: CallbackQuery, data: dict):
        data['user'] = await self.get_userdata(callback_query.from_user.id)


