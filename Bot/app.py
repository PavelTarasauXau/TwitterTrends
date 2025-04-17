
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from .handlers.user_private import user_private_router
from .common.cmd_list import private


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7570599864:AAGHHiX3K7UwRLwryFJv6TKBI-8daoKcx0s"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
dp.include_router(user_private_router)

current_data = {}


async def main_func(data):
    print(data)
    current_data['country'] = data['country']
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    print("🤖 Бот запущен")
    await dp.start_polling(bot)
    asyncio.run(main_func(data))



