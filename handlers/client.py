from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_bot import dp, bot, bot_address
from keyboards.client_kb import kb_client_1, kb_client_2, kb_client_3
from school_database import sqlite_db
from handlers import common

"""Хендлеры для взаимодействия с клиентом
"""


#@dp.message_handler(commands=['start', 'help'])
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

#@dp.message_handler(Text(equals='Привет', ignore_case=True))
async def get_work_hours(message: types.Message):
    common.old_message[message.from_user.id] = False
    await bot.send_message(message.from_user.id, f'2.Люся - бренд-фотограф и рилс-мейкер 7 лет'
                                                 f' профессионально занимается фото и видео съемкой '
                                                 f'Обучила офлайн более 100 человек контентной съемке'
                                                 f' на телефон. Создала курс "Дело в кадре" для обучения'
                                                 f' онлайн Работает с такими брендами, как zaav_g, ognivo '
                                                 f'say da lab На своем канале↘️ Люся  делится фишками по  '
                                                 f'съемке и монтажу + сслыка кнопка на ТГ канал (призыв подписаться)', reply_markup=kb_client_2)



#@dp.message_handler(Text(equals='Далее', ignore_case=True))
async def get_contacts(message: types.Message):
    common.old_message[message.from_user.id] = False
    await bot.send_message(message.from_user.id, f' 3.Фото или видео обращение Люси Снимать на телефон - это не прихоть, а необходимый навык, который пригодиться каждому.\n" \
- людям, которые хотят поменять профессию и зарабатывать на красивом творческом деле\n \
- маме-домохозяйке, чтобы снимать семейные праздники и взросление ребенка\n \
- эксперту и предпринимателю, которые сами ведут акааунты в социальных сетях и продвигаются в онла\n \
Я знаю, как снимать красиво и легко на телефон. Делюсь с вами в коротком практикуме, состоящем из 3-х коротких уроков. \
Смотрите видео прямо сейчас и сразу выполняйте легкие задания, чтобы научиться делать красиввые фото и видео на телефон. \
+кнопка смотреть видео', reply_markup=kb_client_3)



#@dp.message_handler(Text(equals='Смотреть видео', ignore_case=True))
async def get_training_courses(message: types.Message):
    common.old_message[message.from_user.id] = True
    await bot.send_message(message.from_user.id, f'https://www.youtube.com/watch?v=Lc7pjgJkjzo')


async def get_answer(message: types.Message):
    common.old_message[message.from_user.id] = False
    await bot.send_message(message.from_user.id, f' 3.Фото или видео обращение Люси Снимать на телефон - это не прихоть, а необходимый навык, который пригодиться каждому.\n \
- людям, которые хотят поменять профессию и зарабатывать на красивом творческом деле\n \
- маме-домохозяйке, чтобы снимать семейные праздники и взросление ребенка\n \
- эксперту и предпринимателю, которые сами ведут акааунты в социальных сетях и продвигаются в онла\n \
Я знаю, как снимать красиво и легко на телефон. Делюсь с вами в коротком практикуме, состоящем из 3-х коротких уроков. \
Смотрите видео прямо сейчас и сразу выполняйте легкие задания, чтобы научиться делать красиввые фото и видео на телефон. \
+кнопка смотреть видео', reply_markup=kb_client_3)


#@dp.message_handler(Text(equals='Преподаватели', ignore_case=True))
async def get_trainers_info(message: types.Message):
    await sqlite_db.sql_read_from_teachers(message)


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(get_contacts, Text(equals='Далее', ignore_case=True))
    dp.register_message_handler(get_work_hours, Text(equals='Привет', ignore_case=True))
    dp.register_message_handler(get_training_courses, Text(equals='Смотреть видео', ignore_case=True))
    dp.register_message_handler(get_trainers_info, Text(equals='Преподаватели', ignore_case=True))
    dp.register_message_handler(get_answer)