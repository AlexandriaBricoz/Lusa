import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import BotBlocked

from create_bot import dp, bot, bot_address
from keyboards.client_kb import kb_client_1, kb_client_2, kb_client_3, kb_client_6, kb_client_5, kb_client
from school_database import sqlite_db

"""Хендлеры для взаимодействия с клиентом
"""


@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    bot_home = bot_address  # можно указать адрес бота в телеграм строкой 't.me/bot'
    print(message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        f"👋 Привет, {message.from_user.full_name}!\n"
        f"Я бот-помощник Люси Жабиной, контент фотографа.\n"
        f"Прежде чем мы отправимся в мир красивых фото и видео, позволь познакомить тебя с Люсей поближе.",
        reply_markup=kb_client_1
    )

    await message.delete()
    await message.reply(f'Пожалуйста напишите боту в ЛС: {bot_home}')


@dp.message_handler(Text(equals='Привет', ignore_case=True))
async def get_work_hours(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "📸 **Люся** - бренд-фотограф и рилс-мейкер, семь лет профессионально занимается фото и видео съемкой.\n"
                           "🎓 Обучила офлайн более 100 человек контентной съемке на телефон. Создала курс \"Дело в кадре\" для онлайн-обучения.\n"
                           "💼 Работает с такими брендами, как zaav_g, ognivo, say da lab.\n"
                           "🎥 На своем канале Люся делится фишками по съемке и монтажу.\n\n"
                           "🔗 [Ссылка на ТГ канал](<ваша_ссылка>) (призыв подписаться)",
                           reply_markup=kb_client_2)


@dp.message_handler(Text(equals='Далее', ignore_case=True))
async def get_contacts(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "📸 Фото или видео обращение Люси\n\n"
        "Снимать на телефон - это не прихоть, а необходимый навык, который пригодится каждому:\n\n"
        "- Людям, которые хотят поменять профессию и зарабатывать на красивом творческом деле.\n"
        "- Мамам-домохозяйкам, чтобы снимать семейные праздники и взросление ребенка.\n"
        "- Экспертам и предпринимателям, которые сами ведут аккаунты в социальных сетях и продвигаются в онлайн.\n\n"
        "Я знаю, как снимать красиво и легко на телефон. Делюсь с вами в коротком практикуме, состоящем из 3-х коротких уроков.\n"
        "Смотрите видео прямо сейчас и сразу выполняйте легкие задания, чтобы научиться делать красивые фото и видео на телефон.\n\n",
        reply_markup=kb_client_3
    )


class YourStateName(StatesGroup):
    photo_sent = State()
    waiting_for_next_message = State()


timers = {}


@dp.message_handler(Text(equals='Смотреть видео', ignore_case=True))
async def get_training_courses(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=Lc7pjgJkjzo',
                           reply_markup=ReplyKeyboardRemove())
    await bot.send_message(
        message.from_user.id,
        "🕒 Видео доступно всего 24 часа! Посмотрите прямо сейчас. Это займет всего 7 минут.\n\n",
    )

    if message.from_user.id in timers:
        timers[message.from_user.id].cancel()

    timers[message.from_user.id] = asyncio.create_task(wait_for_response(message.from_user.id, state))
    await YourStateName.waiting_for_next_message.set()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=YourStateName.waiting_for_next_message)
async def process_next_message(message: types.Message, state: FSMContext):
    if message.photo:
        cancel_timer(message.from_user.id)
        await bot.send_message(
            message.from_user.id,
            "🎓 А вот и новый урок!\n",
            reply_markup=kb_client_3
        )
        await bot.send_message(message.from_user.id, f'https://www.youtube.com/watch?v=mMqURYfL4Z0',
                               reply_markup=kb_client_6)

        await YourStateName.photo_sent.set()
        await state.reset_state()
    else:
        await bot.send_message(
            message.from_user.id,
            "📸 Вы не отправили фото...\n",
            reply_markup=kb_client_3
        )


async def wait_for_response(user_id, state: FSMContext):
    try:
        await asyncio.sleep(10)  # Исправлено на 10 секунд

        ...
        current_state = await state.get_state()
        if current_state != YourStateName.photo_sent.state:
            await bot.send_message(user_id, "🔥 Ссылка на видео сгорит через 12 часов! Посмотрите, чтобы:\n"
                                            "- Узнать секрет красивых фото и видео.\n"
                                            "- Найти свой уникальный стиль в съемке и выделяться среди других.",
                                   reply_markup=kb_client_3)  # Укажите вашу клавиатуру kb_client_3
    except BotBlocked:
        print(f"Bot was blocked by the user {user_id}")
    finally:
        if user_id in timers:
            del timers[user_id]


def cancel_timer(user_id):
    if user_id in timers:
        timers[user_id].cancel()
        del timers[user_id]


# @dp.message_handler(Text(equals='Преподаватели', ignore_case=True))
async def get_trainers_info(message: types.Message):
    await sqlite_db.sql_read_from_teachers(message)


@dp.message_handler(Text(equals='Супер', ignore_case=True))
async def set_file(message: types.Message):
    file_path = '/Users/aleksey/Desktop/тренажер насмотренности.txt'
    await bot.send_message(
        message.from_user.id,
        "👏 Отлично! Так держать. Вы уже узнали о настройках телефона и разобрались с уникальным стилем в съемке.\n"
        "Приготовила для вас подарок - \"Тренажер насмотренности\". 🎁"
    )
    with open(file_path, 'rb') as document:
        await bot.send_document(chat_id=message.from_user.id, document=document)
    await bot.send_message(message.from_user.id, f'https://www.youtube.com/watch?v=D2S-b4D0IA0',
                           reply_markup=kb_client_5)


@dp.message_handler(Text(equals='Посмотрел', ignore_case=True))
async def set_file(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "🚀 Занять место на курсе \"Дело в кадре\" по самой выгодной цене!\n"
        "Не упустите возможность улучшить свои навыки в фото и видеосъемке.\n\n"
        , reply_markup=kb_client
    )


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(get_contacts, Text(equals='Далее', ignore_case=True))
    dp.register_message_handler(get_work_hours, Text(equals='Привет', ignore_case=True))
    dp.register_message_handler(get_training_courses, Text(equals='Смотреть видео', ignore_case=True))
    dp.register_message_handler(get_trainers_info, Text(equals='Преподаватели', ignore_case=True))
    dp.register_message_handler(get_trainers_info, Text(equals='Супер', ignore_case=True))
