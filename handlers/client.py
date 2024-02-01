import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import BotBlocked

from create_bot import dp, bot, bot_address
from handlers import common
from keyboards.client_kb import kb_client_1, kb_client_2, kb_client_3, kb_client_5
from school_database import sqlite_db

"""Хендлеры для взаимодействия с клиентом
"""


# @dp.message_handler(commands=['start', 'help'])
async def start_bot(message: types.Message):
    common.old_message[message.from_user.id] = False
    bot_home = bot_address  # можно указать адрес бота в телеграм строкой 't.me/bot'
    try:
        await bot.send_message(message.from_user.id,
                               f'1. Привет /Имя/ Я бот-помощник Люси Жабиной контент фотографа '
                               f'Прежде чем мы отправимся в мир красивых фото и видео позволь '
                               f'познакомить тебя с Люсей поближе.', reply_markup=kb_client_1)
        await message.delete()
    except:
        await message.reply(f'Пожалуйста напишите боту в ЛС: {bot_home}')


# @dp.message_handler(Text(equals='Привет', ignore_case=True))
async def get_work_hours(message: types.Message):
    common.old_message[message.from_user.id] = False
    await bot.send_message(message.from_user.id, f'2.Люся - бренд-фотограф и рилс-мейкер 7 лет'
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
    await bot.send_message(message.from_user.id, f' 3.Фото или видео обращение Люси Снимать на телефон - это не прихоть, а необходимый навык, который пригодиться каждому.\n" \
- людям, которые хотят поменять профессию и зарабатывать на красивом творческом деле\n \
- маме-домохозяйке, чтобы снимать семейные праздники и взросление ребенка\n \
- эксперту и предпринимателю, которые сами ведут акааунты в социальных сетях и продвигаются в онла\n \
Я знаю, как снимать красиво и легко на телефон. Делюсь с вами в коротком практикуме, состоящем из 3-х коротких уроков. \
Смотрите видео прямо сейчас и сразу выполняйте легкие задания, чтобы научиться делать красиввые фото и видео на телефон. \
+кнопка смотреть видео', reply_markup=kb_client_3)


# Предположим, что вы создали объект dp (Dispatcher), db (Database) и loop (EventLoop) в вашем коде

# Создаем состояние для ожидания следующего сообщения
class YourStateName(StatesGroup):
    waiting_for_next_message = State()

# Обработчик команды "Смотреть видео"
@dp.message_handler(Text(equals='Смотреть видео', ignore_case=True))
async def get_training_courses(message: types.Message):
    # Сохраняем текущее сообщение в базу данных

    # Посылаем ссылку на видео и убираем клавиатуру
    await bot.send_message(message.from_user.id, f'https://www.youtube.com/watch?v=Lc7pjgJkjzo',
                           reply_markup=ReplyKeyboardRemove())

    # Ожидаем следующее сообщение
    await YourStateName.waiting_for_next_message.set()

    # Запускаем таймер на 2 минуты
    asyncio.create_task(wait_for_response(message.from_user.id))

# Обработчик следующего сообщения после команды "Смотреть видео"
@dp.message_handler(state=YourStateName.waiting_for_next_message)
async def process_next_message(message: types.Message, state: FSMContext):
    # Сохраняем следующее сообщение в базу данных
    await save_message_to_db(message)

    # Сбрасываем состояние
    await state.finish()

    # Далее ваш код обработки следующего сообщения

    # Отменяем таймер, так как ответ получен
    cancel_timer(message.from_user.id)

async def save_message_to_db(message: types.Message):
    # Ваш код для сохранения сообщения в базу данных
    user_id = message.from_user.id
    text = message.text
    print(user_id,text)
    # Дополнительные действия по сохранению в базе данных
    # Например, используйте ORM, если у вас есть модели данных
    # Или подходящую технологию для ваших потребностей
    await bot.send_message(user_id, f'Отлично! Так держать. Вы уже узнали о настройках телефона и'
                                    f' разобрались с уникальным стилем в съемке. Приготовила для'
                                    f' вас подарок "тренажер насмотренности"')

async def wait_for_response(user_id):
    await asyncio.sleep(30)  # Ожидаем 30 секунд

    try:
        # Отправляем напоминание
        await bot.send_message(user_id, "Ссылка на видео сгорит через 12 часов. Посмотрите, чтобы:"
                                        "\n- узнать секрет красивых фото и видео"
                                        "\n- найти свой уникальный стиль в съемке и выделяться среди других", reply_markup=kb_client_3)
    except BotBlocked:
        # Обработка исключения, если бот заблокирован пользователем
        pass

def cancel_timer(user_id):
    # Отменяем таймер, если ответ получен
    # Если используете asyncio.ensure_future, можно также использовать task.cancel()
    # В данном примере мы просто удаляем таймер из очереди выполнения asyncio
    for task in asyncio.all_tasks():
        if task.get_coro() == wait_for_response and task.get_coro().cr_frame.f_locals['user_id'] == user_id:
            task.cancel()
# async def get_answer(message: types.Message):
#     common.old_message[message.from_user.id] = False



# @dp.message_handler(Text(equals='Преподаватели', ignore_case=True))
async def get_trainers_info(message: types.Message):
    await sqlite_db.sql_read_from_teachers(message)


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(get_contacts, Text(equals='Далее', ignore_case=True))
    dp.register_message_handler(get_work_hours, Text(equals='Привет', ignore_case=True))
    dp.register_message_handler(get_training_courses, Text(equals='Смотреть видео', ignore_case=True))
    dp.register_message_handler(get_trainers_info, Text(equals='Преподаватели', ignore_case=True))
