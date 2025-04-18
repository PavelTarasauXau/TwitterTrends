
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

from aiogram import F, types, Router
from aiogram.enums import ContentType
from aiogram.types import FSInputFile
from Bot.kbds import reply


# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7570599864:AAGHHiX3K7UwRLwryFJv6TKBI-8daoKcx0s"
current_data = {}


# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
dp.include_router(user_private_router)

# главный хэндлер - он должен работать с передаваемым данными
@dp.message(F.text.in_(['Cali','Family','Football','High_school','Movie','Shopping','Snow','Texas','Weekend']))
async def choose_command_handler(message: types.Message):
    current_data['comobox'].set(message.text)
    current_data['selected']()
    await message.answer('лови')
    photo = FSInputFile(f"C:\\Users\\tazhu\\PycharmProjects\\OOP_project\\Data\\imgs\\screenshot.png")
    await message.reply_photo(photo,reply_markup=reply.after_screen_kb)
    await message.answer(f'по тематике {message.text} было обработано <b>{len(current_data["parser"].tweets)}</b> твиттов')

@dp.message(F.text == "Самый 'позитивный' штат" )
async def choose_command_handler(message: types.Message):
    most_positive_state = None
    max_sentiment = 0
    for state in current_data['country'].states:
        if state.sentiment != None:
            if state.sentiment > max_sentiment:
                max_sentiment = state.sentiment
                most_positive_state = state
    await message.answer(f'Cамый <i>позитивный</i> штат - <b>{most_positive_state.name}</b>\n'
                         f'\nКоличество постов сделанных в этом штате - <b>{len(most_positive_state.tweets)}</b>',parse_mode='HTML',
                         reply_markup=reply.after_screen_kb)

@dp.message(F.text == "Самый 'негативный' штат" )
async def choose_command_handler(message: types.Message):
    most_negative_state = None
    min_sentiment = 0
    for state in current_data['country'].states:
        if state.sentiment != None:
            if state.sentiment < min_sentiment:
                min_sentiment = state.sentiment
                most_negative_state = state
    await message.answer(f'самый <i>негативный</i> штат - <b>{most_negative_state.name}</b>\n'
                         f'\nКоличество постов сделанных в этом штате - <b>{len(most_negative_state.tweets)}</b>',parse_mode='HTML',
                         reply_markup=reply.after_screen_kb)

@dp.message(F.text == "Самый 'активный' штат" )
async def choose_command_handler(message: types.Message):
    most_active_state = None
    most_tweets = len(current_data['country'].states[0].tweets)
    for state in current_data['country'].states:
        if len(state.tweets) > most_tweets:
            most_tweets = len(state.tweets)
            most_active_state = state
    await message.answer(f'самый <i>активный</i> штат - <b>{most_active_state.name}</b>\n'
                         f'\nКоличество постов сделанных в этом штате - <b>{len(most_active_state.tweets)}</b>',parse_mode='HTML',
                         reply_markup=reply.after_screen_kb)

@dp.message(F.text == "Самый 'неактивный' штат" )
async def choose_command_handler(message: types.Message):
    most_unactive_state = None
    most_tweets = len(current_data['country'].states[0].tweets)
    for state in current_data['country'].states:
        if len(state.tweets) < most_tweets:
            most_tweets = len(state.tweets)
            most_unactive_state = state
    await message.answer(f'самый <i>активный</i> штат - <b>{most_unactive_state.name}</b>\n'
                         f'\nКоличество постов сделанных в этом штате - <b>{len(most_unactive_state.tweets)}</b>',parse_mode='HTML',
                         reply_markup=reply.after_screen_kb)


@dp.message(F.text == "Показать твитты на карте" )
async def choose_command_handler(message: types.Message):
    current_data['drawer'].draw_tweets()
    await message.answer('Сделано. Вот карта с твиттами:')
    photo = FSInputFile(f"C:\\Users\\tazhu\\PycharmProjects\\OOP_project\\Data\\imgs\\screenshot.png")
    await message.reply_photo(photo,reply_markup=reply.after_screen_kb_and_show_tweets)

@dp.message(F.text == "Скрыть твитты на карте" )
async def choose_command_handler(message: types.Message):
    current_data['drawer'].delete_tweets()
    await message.answer('Сделано. Вот карта без твиттов:')
    photo = FSInputFile(f"C:\\Users\\tazhu\\PycharmProjects\\OOP_project\\Data\\imgs\\screenshot.png")
    await message.reply_photo(photo,reply_markup=reply.after_screen_kb)







async def main_func(data):
    current_data['comobox'] = data['comobox']
    current_data['country'] = data['country']
    current_data['selected'] = data['selected']
    current_data['drawer'] = data['drawer']
    current_data['parser'] = data['parser']
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(commands=private,scope=types.BotCommandScopeAllPrivateChats())
    print("🤖 Бот запущен")
    await dp.start_polling(bot)
    asyncio.run(main_func(data))



