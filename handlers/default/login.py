from aiogram.types import Message
from models.user import User
from middlewares.userdata import userdata_required


@userdata_required
async def login_test(msg: Message, user: User):
    await msg.answer(f'Howdy, {msg.from_user.full_name} with id {user.id} created at {user.created_at}?')
