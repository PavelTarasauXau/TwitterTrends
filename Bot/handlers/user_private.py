from aiogram import F, types, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold #Italic, as_numbered_list и тд
from aiogram.types import Message
from aiogram.enums import ContentType
from aiogram.types import FSInputFile

from Bot.kbds import reply

user_private_router = Router()

@user_private_router.message(CommandStart())
@user_private_router.message(F.text == 'В главное меню')
async def start_cmd(message: types.Message):
    print(message.text)
    await message.answer("Привет, я виртуальный помощник",reply_markup=reply.start_kb)

@user_private_router.message(F.text == 'Выбрать тему твитта')
@user_private_router.message(F.text == 'Вернуться к выбору тем')
async def choose_command_handler(message: types.Message):
    await message.answer("Хорошо, выбирай из предложенных", reply_markup=reply.tweet_topics_kb)

@user_private_router.message(F.text.in_(['Cali','Family','Football','High_school','Movie','Shopping','Snow','Texas','Weekend']))
async def choose_command_handler(message: types.Message):
    await message.answer('ок, держи карту')
    photo = FSInputFile(f"C:\\Users\\tazhu\PycharmProjects\OOP_project\Data\imgs\\screenshot.png")
    await message.reply_photo(photo,reply_markup=reply.after_screen_kb)

