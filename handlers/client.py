import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import BotBlocked

from create_bot import dp, bot, bot_address
from keyboards.client_kb import kb_client_1, kb_client_3, kb_client_5, kb_client


class YourStateName(StatesGroup):
    photo_sent = State()
    waiting_for_next_message = State()


timers = {}

"""Хендлеры для взаимодействия с клиентом
"""


@dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    bot_home = bot_address  # можно указать адрес бота в телеграм строкой 't.me/bot'
    print(message.from_user.id)
    await bot.send_message(
        message.from_user.id,
        f"👋 Привет, {message.from_user.full_name}!\n\n"
        f"Я бот-помощник Люси Жабиной - brend фотографа и контент-мейкера.\n"
        f"Прежде чем мы отправимся в мир красивых фото и видео позволь познакомить тебя с Люсей поближе ⤵️",
        reply_markup=kb_client_1
    )
    await message.delete()


@dp.message_handler(Text(equals='👋 Привет', ignore_case=True))
async def hi(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'https://youtube.com/shorts/_KGZjDVQat4?si=S7t8ElorE7RJ-s2r',
                           reply_markup=kb_client_3)
    await bot.send_message(message.from_user.id,
                           "🔺7 лет профессионально занимается фото и видео съемкой\n"
                           "🔺Обучила офлайн более 100 человек контентной съемке на телефон.\n"
                           '🔺Создала курс "Дело в кадре" для обучения онлайн\n'
                           "🔺Работает с такими брендами, как zaav_g, ognivo, say da lab, YNE \n\n"
                           "На своем канале  Люся делится фишками по съемке и монтажу\n"
                           "Подпишись и возвращайся сюда, чтобы получить 3 урока по контентной съемке\n"
                           "⤵️⤵️⤵️\n"
                           'https://t.me/lusy_zhabina',
                           reply_markup=kb_client_3)


@dp.message_handler(Text(equals='📹 Смотреть видео', ignore_case=True))
async def video_1(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'https://youtu.be/L1pWz0YEogM?si=nW8s0-Gd-prhWC9F',
                           reply_markup=ReplyKeyboardRemove())
    await bot.send_message(
        message.from_user.id,
        "‼️ Видео доступно всего 24 часа.\n"
        " Посмотрите прямо сейчас. Это займет всего ... (время видео 1)  минут",
        reply_markup=ReplyKeyboardRemove()
    )
    await bot.send_message(
        message.from_user.id,
        "Сначала отправьте фото сделанное с сеткой",
        reply_markup=ReplyKeyboardRemove()
    )
    if message.from_user.id in timers:
        timers[message.from_user.id].cancel()
    timers[message.from_user.id] = asyncio.create_task(wait_for_response(message.from_user.id, state))
    await YourStateName.waiting_for_next_message.set()


@dp.message_handler(content_types=types.ContentTypes.PHOTO, state=YourStateName.waiting_for_next_message)
async def video_2(message: types.Message, state: FSMContext):
    if message.photo:
        async with state.proxy() as data:
            if "first_photo" not in data:
                # Если это первое фото, сохраняем его
                data["first_photo"] = message.photo[-1].file_id
                await bot.send_message(
                    message.from_user.id,
                    'Круто! Теперь без сетки'
                )
            else:
                await bot.send_message(
                    message.from_user.id,
                    "👏 Отлично! Так держать. "
                    "Вы уже узнали о настройках телефона и разобрались с уникальным стилем в съемке.\n"
                    # "Приготовила для вас подарок - \"Тренажер насмотренности\". 🎁"
                )
                await bot.send_message(message.from_user.id, f'https://youtu.be/peGVJ56U3P0?si=URVYTYDOmIveOFvJ',
                                       reply_markup=ReplyKeyboardRemove())
                await state.finish()  # Завершаем состояние
                cancel_timer(message.from_user.id)
    else:
        await bot.send_message(
            message.from_user.id,
            "📸 Пожалуйста, отправьте фото..."
        )


async def wait_for_response(user_id, state: FSMContext):
    try:
        await asyncio.sleep(10)  # Исправлено на 10 секунд
        current_state = await state.get_state()
        if current_state != YourStateName.photo_sent.state:
            await bot.send_message(user_id,
                                   "‼️Напоминание Ссылка на видео сгорит через 12 часов.Посмотрите, чтобы:\n"
                                   "- узнать секрет красивых фото и видео- найти свой уникальный стиль в съемке\n"
                                   "- начать выделяться контентом среди других\n",
                                   reply_markup=ReplyKeyboardRemove())  # Укажите вашу клавиатуру kb_client_3
    except BotBlocked:
        print(f"Bot was blocked by the user {user_id}")
    finally:
        if user_id in timers:
            del timers[user_id]


@dp.message_handler(Text(equals='Лайфхак', ignore_case=True))
async def video_3(message: types.Message):
    file_path = '/Users/aleksey/Desktop/тренажер насмотренности.txt'
    with open(file_path, 'rb') as document:
        await bot.send_document(
            chat_id=message.from_user.id,
            document=document,
            caption="Приготовила для вас подарок - \"Тренажер насмотренности\". 🎁",
            reply_markup=ReplyKeyboardRemove()
        )
    await bot.send_message(message.from_user.id, f'https://youtu.be/_bY3rY2Vi2w?si=udLXMDjmeNkKUzdd',
                           reply_markup=kb_client_5)


@dp.message_handler(Text(equals='лайфхак', ignore_case=True))
async def video_3_1(message: types.Message):
    file_path = '/Users/aleksey/Desktop/тренажер насмотренности.txt'
    with open(file_path, 'rb') as document:
        await bot.send_document(
            chat_id=message.from_user.id,
            document=document,
            caption="Приготовила для вас подарок - \"Тренажер насмотренности\". 🎁",
            reply_markup=ReplyKeyboardRemove()
        )
    await bot.send_message(message.from_user.id, f'https://youtu.be/_bY3rY2Vi2w?si=udLXMDjmeNkKUzdd',
                           reply_markup=kb_client_5)


def cancel_timer(user_id):
    if user_id in timers:
        timers[user_id].cancel()
        del timers[user_id]


@dp.message_handler(Text(equals='💼 Познакомиться с тарифами', ignore_case=True))
async def get_tariffs(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        '♨️ Занять место на курсе "Дело в кадре" по самой выгодной цене'
        , reply_markup=kb_client
    )


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(hi, Text(equals='👋 Привет', ignore_case=True))
    dp.register_message_handler(video_1, Text(equals='📹 Смотреть видео', ignore_case=True))
    dp.register_message_handler(get_tariffs, Text(equals='💼 Познакомиться с тарифами', ignore_case=True))
    dp.register_message_handler(video_3, Text(equals='Лайфхак', ignore_case=True))
    dp.register_message_handler(video_3_1, Text(equals='лайфхак', ignore_case=True))
