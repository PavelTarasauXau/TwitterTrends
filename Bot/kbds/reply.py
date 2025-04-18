
from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Выбрать тему твитта"),
            KeyboardButton(text="О нас"),
        ],
        [KeyboardButton(text="Наши контакты")]
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



about_us_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="В главное меню")]

    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)
contacts_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="В главное меню")]

    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)




after_screen_kb = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Показать твитты на карте")],
            [KeyboardButton(text="Вернуться к выбору тем")],
            [KeyboardButton(text="Самый 'позитивный' штат")],
            [KeyboardButton(text="Самый 'негативный' штат")],
            [KeyboardButton(text="Самый 'активный' штат")],
            [KeyboardButton(text="Самый 'неактивный' штат")]
    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)

after_screen_kb_and_show_tweets = ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton(text="Скрыть твитты на карте")],
            [KeyboardButton(text="Вернуться к выбору тем")],
            [KeyboardButton(text="Самый 'позитивный' штат")],
            [KeyboardButton(text="Самый 'негативный' штат")],
            [KeyboardButton(text="Самый 'активный' штат")],
            [KeyboardButton(text="Самый 'неактивный' штат")]
    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)




