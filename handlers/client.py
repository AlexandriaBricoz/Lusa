import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import BotBlocked

from create_bot import dp, bot, bot_address
from handlers import common
from keyboards.client_kb import kb_client_1, kb_client_2, kb_client_3
from school_database import sqlite_db

"""Хендлеры для взаимодействия с клиентом
"""


# @dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    common.old_message[message.from_user.id] = False
    bot_home = bot_address  # можно указать адрес бота в телеграм строкой 't.me/bot'
    try:
        await bot.send_message(message.from_user.id,
                               f'Привет, {message.from_user.full_name}, Я бот-помощник Люси Жабиной контент фотографа '
                               f'Прежде чем мы отправимся в мир красивых фото и видео позволь '
                               f'познакомить тебя с Люсей поближе.', reply_markup=kb_client_1)
        await message.delete()
    except:
        await message.reply(f'Пожалуйста напишите боту в ЛС: {bot_home}')


# @dp.message_handler(Text(equals='Привет', ignore_case=True))
async def get_work_hours(message: types.Message):
    common.old_message[message.from_user.id] = False
    await bot.send_message(message.from_user.id, f'Люся - бренд-фотограф и рилс-мейкер 7 лет'
                                                 f' профессионально занимается фото и видео съемкой '
                                                 f'Обучила офлайн более 100 человек контентной съемке'
                                                 f' на телефон. Создала курс "Дело в кадре" для обучения'
                                                 f' онлайн Работает с такими брендами, как zaav_g, ognivo '
                                                 f'say da lab На своем канале↘️ Люся  делится фишками по  '
                                                 f'съемке и монтажу + сслыка кнопка на ТГ канал (призыв подписаться)',
                           reply_markup=kb_client_2)


# @dp.message_handler(Text(equals='Далее', ignore_case=True))
async def get_contacts(message: types.Message):
    common.old_message[message.from_user.id] = False
    await bot.send_message(message.from_user.id, f' Фото или видео обращение Люси Снимать на телефон - это не прихоть, а необходимый навык, который пригодиться каждому.\n" \
- людям, которые хотят поменять профессию и зарабатывать на красивом творческом деле\n \
- маме-домохозяйке, чтобы снимать семейные праздники и взросление ребенка\n \
- эксперту и предпринимателю, которые сами ведут акааунты в социальных сетях и продвигаются в онла\n \
Я знаю, как снимать красиво и легко на телефон. Делюсь с вами в коротком практикуме, состоящем из 3-х коротких уроков. \
Смотрите видео прямо сейчас и сразу выполняйте легкие задания, чтобы научиться делать красиввые фото и видео на телефон. \
+кнопка смотреть видео', reply_markup=kb_client_3)


file_path = '/Users/aleksey/Desktop/File.txt'
...


# Инициализация бота и диспетчера здесь (пример):
# bot = Bot(token='YOUR_BOT_TOKEN')
# dp = Dispatcher(bot)

class YourStateName(StatesGroup):
    photo_sent = State()
    waiting_for_next_message = State()


timers = {}


@dp.message_handler(Text(equals='Смотреть видео', ignore_case=True))
async def get_training_courses(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=Lc7pjgJkjzo',
                           reply_markup=ReplyKeyboardRemove())
    await bot.send_message(message.from_user.id,
                           'Видео доступно всего 24 часа. Посмотрите прямо сейчас. Это займет всего ... 7 минут + кнопка смотреть видео',
                           reply_markup=kb_client_3)

    if message.from_user.id in timers:
        timers[message.from_user.id].cancel()

    timers[message.from_user.id] = asyncio.create_task(wait_for_response(message.from_user.id, state))
    await YourStateName.waiting_for_next_message.set()


@dp.message_handler(state=YourStateName.waiting_for_next_message)
async def process_next_message(message: types.Message, state: FSMContext):
    if message.text == '0':
        cancel_timer(message.from_user.id)
        await bot.send_message(message.from_user.id, f'https://www.youtube.com/watch?v=mMqURYfL4Z0')
        await asyncio.sleep(10)
        file_path = '/Users/aleksey/Desktop/тренажер насмотренности.txt'
        await bot.send_message(message.from_user.id, f'Отлично! Так держать. Вы уже узнали о настройках телефона и'
                                                     f' разобрались с уникальным стилем в съемке. Приготовила для'
                                                     f' вас подарок "тренажер насмотренности"')
        with open(file_path, 'rb') as document:
            await bot.send_document(chat_id=message.from_user.id, document=document, caption='Описание к фото')

        await YourStateName.photo_sent.set()
        await state.reset_state()
    else:
        await bot.send_message(message.from_user.id, "Вы не отправили фото...",
                               reply_markup=kb_client_3)  # Укажите вашу клавиатуру kb_client_


# ...продолжение предыдущего сообщения

async def wait_for_response(user_id, state: FSMContext):
    try:
        await asyncio.sleep(10)  # Исправлено на 10 секунд

        ...
        current_state = await state.get_state()
        if current_state != YourStateName.photo_sent.state:
            await bot.send_message(user_id, "Ссылка на видео сгорит через 12 часов. Посмотрите, чтобы:"
                                            "\n- узнать секрет красивых фото и видео"
                                            "\n- найти свой уникальный стиль в съемке и выделяться среди других",
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


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(get_contacts, Text(equals='Далее', ignore_case=True))
    dp.register_message_handler(get_work_hours, Text(equals='Привет', ignore_case=True))
    dp.register_message_handler(get_training_courses, Text(equals='Смотреть видео', ignore_case=True))
    dp.register_message_handler(get_trainers_info, Text(equals='Преподаватели', ignore_case=True))
