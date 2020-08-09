from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger
from tortoise import Tortoise

import config
import handlers
import middlewares

storage = MemoryStorage()
telegram_bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(telegram_bot, storage=storage)


def on_startup():
    logger.info("Register handlers...")
    # Register you handlers here.
    handlers.default.setup(dp)
    dp.middleware.setup(middlewares.UserMiddleware())


async def database_init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={
            'model': ['models.user']
        }
    )
    await Tortoise.generate_schemas()
    logger.info("Tortoise inited!")


if __name__ == "__main__":
    on_startup()
    dp.loop.create_task(database_init())
    executor.start_polling(dp, skip_updates=True)
