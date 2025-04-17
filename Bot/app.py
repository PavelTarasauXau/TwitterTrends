
import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = ""

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

current_data = {}

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.italic(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message):
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received
        await message.answer(current_data['country'].states[0].name)
        await message.answer(str(current_data['country'].states[0].tweets))
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main_func(data):
    print(data)
    current_data['country'] = data['country']
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    print("🤖 Бот запущен")
    await dp.start_polling(bot)
    asyncio.run(main_func(data))



