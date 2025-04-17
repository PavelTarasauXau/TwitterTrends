
from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выбрать тему твитта"),
            KeyboardButton(text="О нас"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)

tweet_topics_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Cali")],
            [KeyboardButton(text="Family")],
            [KeyboardButton(text="Football")],
            [KeyboardButton(text="High_school")],
            [KeyboardButton(text="Movie")],
            [KeyboardButton(text="Shopping")],
            [KeyboardButton(text="Snow")],
            [KeyboardButton(text="Texas")],
            [KeyboardButton(text="Weekend")],
            [KeyboardButton(text="В главное меню")]

    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)

after_screen_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Вернуться к выбору тем")],
            [KeyboardButton(text="Статистика по штатам")],
            [KeyboardButton(text="Показать твитты")]
    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)

