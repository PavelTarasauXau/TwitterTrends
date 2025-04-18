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
    await message.answer("Привет, выбирай пункт меню, чтобы продолжить",reply_markup=reply.start_kb)

@user_private_router.message(Command('about'))
@user_private_router.message(F.text == 'О нас')
async def start_cmd(message: types.Message):
    await message.answer('''Добро пожаловать в наш телеграм-бот, который позволяет вам глубже понять социальные настроения по штатам США через анализ твитов! Мы создаём уникальную платформу, где вы можете просматривать статистику твитов, легко доступную на удобной карте. 

Наша цель – предоставить вам актуальные и достоверные данные о тенденциях, мнениях и обсуждениях, которые волнуют граждан в каждом штате. Мы собираем информацию в реальном времени, чтобы вы могли видеть, что происходит в социальной сети Twitter.

С помощью нашего бота вы можете:
- Исследовать статистику твитов по каждому штату
- Получать информацию о горячих темах обсуждений
- Узнавать, какие настроения преобладают в различных регионах

Присоединяйтесь к нам и оставайтесь в курсе общественного мнения с нашим интуитивно понятным интерфейсом и наглядной картой!''',reply_markup=reply.about_us_kb)

@user_private_router.message(Command('contacts'))
@user_private_router.message(F.text == 'Наши контакты')
async def start_cmd(message: types.Message):
    await message.answer('''
Если вы хотите с нами пообщаться, задать вопросы или просто поделиться впечатлениями, мы всегда на связи! 

Пишите нам, если:
- Вы нашли баг (который не состоит из крабов, не переживайте, мы никого не обидим!)
- У вас есть идея, как сделать наш бот еще круче (или даже если не круче, просто «круто»)
- Вы хотите рассказать, как ваш твит стал вирусным и зацепил все штаты (возможно, у вас есть секретный рецепт?)
- Или если вам просто нужно поговорить о любимых мемах! 

Github - https://github.com/PavelTarasauXau/TwitterTrends
mail - twitter_trends_team@mail.ru
Алексей селезнёв - тавлая 52''',reply_markup=reply.about_us_kb)


@user_private_router.message(Command('menu'))
async def start_cmd(message: types.Message):
    await message.answer("Привет, я виртуальный помощник",reply_markup=reply.start_kb)

@user_private_router.message(F.text == 'Выбрать тему твитта')
@user_private_router.message(F.text == 'Вернуться к выбору тем')
async def choose_command_handler(message: types.Message):
    await message.answer("Хорошо, выбирай из предложенных", reply_markup=reply.tweet_topics_kb)






