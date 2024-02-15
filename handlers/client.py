import asyncio

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.exceptions import BotBlocked

from create_bot import dp, bot, bot_address
from keyboards.client_kb import kb_client_1, kb_client_3, kb_client_5, keyboard_tg, kb_client_next, kb_client, pay_3, \
    pay_2, pay_1


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
    # await bot.send_message(message.from_user.id,
    #                        'https://youtube.com/shorts/_KGZjDVQat4?si=S7t8ElorE7RJ-s2r',
    # reply_markup=kb_client_3)
    await bot.send_message(message.from_user.id,
                           "🔺7 лет профессионально занимается фото и видео съемкой\n"
                           "🔺Обучила офлайн более 100 человек контентной съемке на телефон.\n"
                           '🔺Создала курс "Дело в кадре" для обучения онлайн\n'
                           "🔺Работает с такими брендами, как zaav_g, ognivo, say da lab, YNE \n\n"
                           "На своем канале  Люся делится фишками по съемке и монтажу\n"
                           "Подпишись и возвращайся сюда, чтобы получить 3 урока по контентной съемке\n"
                           "⤵️⤵️⤵️\n",
                           reply_markup=keyboard_tg)
    await bot.send_message(message.from_user.id,
                           "Подписывайся и возвращайся",
                           reply_markup=kb_client_next)


@dp.message_handler(Text(equals='Продолжить', ignore_case=True))
async def next(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'https://youtube.com/shorts/_KGZjDVQat4?si=S7t8ElorE7RJ-s2r',
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
        await asyncio.sleep(900)  # Исправлено на 10 секунд
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
    file_path = 'Список для тренировки насмотрености.pdf'
    with open(file_path, 'rb') as document:
        await bot.send_document(
            chat_id=message.from_user.id,
            document=document,
            caption="Приготовила для вас подарок - \"Список для тренировки насмотрености\". 🎁",
            reply_markup=ReplyKeyboardRemove()
        )
    await bot.send_message(message.from_user.id, f'https://youtu.be/_bY3rY2Vi2w?si=udLXMDjmeNkKUzdd',
                           reply_markup=kb_client_5)
    await bot.send_message(
        message.from_user.id,
        '''Ты посмотрел 3 урока, которые познакомили тебя с основами контентной съемки. 
Как говорила Люся: “Красиво снимать может каждый! Важно знать основу и практиковать”

Этим мы займемся на курсе “Дело в кадре”
Посмотри программу, чтобы решить, хочешь ли ты погрузиться в мир фото и видео подробнее

Ознакомиться с программой курса 
'''
        , reply_markup=kb_client_5
    )


@dp.message_handler(Text(equals='лайфхак', ignore_case=True))
async def video_3_1(message: types.Message):
    file_path = 'Список для тренировки насмотрености.pdf'
    with open(file_path, 'rb') as document:
        await bot.send_document(
            chat_id=message.from_user.id,
            document=document,
            caption="Приготовила для вас подарок - \"Список для тренировки насмотрености\". 🎁",
            reply_markup=ReplyKeyboardRemove()
        )
    await bot.send_message(message.from_user.id, f'https://youtu.be/_bY3rY2Vi2w?si=udLXMDjmeNkKUzdd',
                           reply_markup=ReplyKeyboardRemove())
    await bot.send_message(
        message.from_user.id,
        '''Ты посмотрел 3 урока, которые познакомили тебя с основами контентной съемки. 
Как говорила Люся: “Красиво снимать может каждый! Важно знать основу и практиковать”

Этим мы займемся на курсе “Дело в кадре”
Посмотри программу, чтобы решить, хочешь ли ты погрузиться в мир фото и видео подробнее

Ознакомиться с программой курса 
'''
        , reply_markup=kb_client_5
    )


@dp.callback_query_handler(lambda c: c.data.startswith('tariff'))
async def process_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()
    data = callback_query.data
    if data == "tariffs":
        await callback_query.message.reply(
            '''Модуль 1 "Настройки камеры"
    ✔️ Вы узнаете:
    - для чего нужны и почему важны правильные настройки
    - где они находятся и как их использовать
    - в каких случаях их нужно применять и какой результат они дают
    ✔️ Сделаете сразу правильные настройки для дальнейшей работы и качественной съемки
    ✔️ Познакомитесь с сеткой и разберетесь, как ее применять.

    Модуль 2 "Правила съемки"
     Свет
    ✔️  Научитесь видеть правильный свет и нужные ракурсы, чтобы разнообразить съемки
    ✔️  Узнаете, какие ошибки бывают при неправильном использовании света 

    Композиция
    ✔️ Научитесь видеть красивый кадр
    ✔️ Примените правила для составления  композиции на практике
    ✔️ Узнаете виды композиций

    Визуал
    ✔️ Узнаете, как собрать кадры в единую красивую стильную ленту 
    ✔️ Разберетесь в основных правилах построения визуала
    ✔️ Познакомитесь с актуальными трендами 2023 года

    Главный результат:
    ✔️ Научитесь находить красивые кадры и отработаете этот навык на практике
    ✔️ Сможете составить красивую картинку из своих фотографий

    Модуль 3 "Обработка"
    ✔️ Узнаете:
    - на что обращать внимание при обработке фото и видео
    - как делать обработку незаметной и естественной

    ✔️ Научитесь:
    - корректировать цвет и свет на фотографии
    - деликатно изменять пропорции тела
    - обрабатывать и устранять недостатки кожи
    - адекватно использовать фильтры

    ✔️ Получите список программ для обработки и коррекции

    '''
            , reply_markup=kb_client
        )
        await callback_query.message.reply(
            '''Отлично! Теперь осталось определиться с тарифом
    Читай описание и занимай место прямо сейчас по выгодной цене
    '''
            , reply_markup=kb_client
        )
    elif data == "tariff_1_1":
        await bot.send_message(1324829412, f'Отлично! После проверки оплаты, с вами свяжутся')
        await bot.send_message(1324829412, f'Была попытка оплатить тариф тариф "САМОСТОЯТЕЛЬНЫЙ"\n'
                                           f'id пользователя: {callback_query.from_user.id}\n'
                                           f'ФИ пользователя: {callback_query.from_user.full_name}\n'
                                           f'Ник пользователя: {callback_query.from_user.username}\n')
    elif data == "tariff_2_1":
        await bot.send_message(1324829412, f'Отлично! После проверки оплаты, с вами свяжутся')
        await bot.send_message(1324829412, f'Была попытка оплатить тариф "С КУРАТОРОМ"\n'
                                           f'id пользователя: {callback_query.from_user.id}\n'
                                           f'ФИ пользователя: {callback_query.from_user.full_name}\n'
                                           f'Ник пользователя: {callback_query.from_user.username}\n')
    elif data == "tariff_3_1":
        await bot.send_message(1324829412, f'Отлично! После проверки оплаты, с вами свяжутся')
        await bot.send_message(1324829412, f'Была попытка оплатить тариф тариф "С ЛЮСЕЙ"\n'
                                           f'id пользователя: {callback_query.from_user.id}\n'
                                           f'ФИ пользователя: {callback_query.from_user.full_name}\n'
                                           f'Ник пользователя: {callback_query.from_user.username}\n')


@dp.message_handler(Text(equals='Кнопка Тариф "САМОСТОЯТЕЛЬНЫЙ', ignore_case=True))
async def tariff_1(message: types.Message):
    await bot.send_message(message.from_user.id, """Тариф "САМОСТОЯТЕЛЬНЫЙ"

Что входит в обучение:
• Доступ к урокам 3 месяца
• База дополнительных материалов
• Домашние задания без проверки
• Общий чат с участниками
 
Стоимость: 14 490
Кнопка оплатить 14 490
""", reply_markup=pay_1)


@dp.message_handler(Text(equals='Тариф "С КУРАТОРОМ"', ignore_case=True))
async def tariff_2(message: types.Message):
    await bot.send_message(message.from_user.id, """Тариф "С КУРАТОРОМ"
Что входит в обучение:
• Доступ к урокам 3 месяца
• База дополнительных материалов
• Домашние задания с проверкой куратора
• Общий чат с участниками
• Участие в воркшопе "Как снимать дорого"
• Сертификат о прохождении курса

Стоимость: 23 490
""", reply_markup=pay_2)


@dp.message_handler(Text(equals='Тариф "С ЛЮСЕЙ"', ignore_case=True))
async def tariff_3(message: types.Message):
    # await bot.send_message(message.from_user.id,
    #                        'https://youtube.com/shorts/_KGZjDVQat4?si=S7t8ElorE7RJ-s2r',
    # reply_markup=kb_client_3)
    await bot.send_message(message.from_user.id, """Тариф "С ЛЮСЕЙ"

Что входит в обучение:
• Доступ к урокам 3 месяца
• База дополнительных материалов
• Домашние задания с проверкой куратора
• Общий чат с участниками
• Отдельный чат с Люсей
• Сертификат о прохождении курса
• Участие в воркшопе "Как снимать дорого"

Стоимость: 35 490
""", reply_markup=pay_3)


def cancel_timer(user_id):
    if user_id in timers:
        timers[user_id].cancel()
        del timers[user_id]


def handlers_register(dp: Dispatcher):
    dp.register_message_handler(start_bot, commands=['start', 'help'])
    dp.register_message_handler(hi, Text(equals='👋 Привет', ignore_case=True))
    dp.register_message_handler(video_1, Text(equals='📹 Смотреть видео', ignore_case=True))
    dp.register_message_handler(video_3, Text(equals='Лайфхак', ignore_case=True))
    dp.register_message_handler(video_3_1, Text(equals='лайфхак', ignore_case=True))
    dp.register_message_handler(tariff_1, Text(equals='Тариф "САМОСТОЯТЕЛЬНЫЙ"', ignore_case=True))
    dp.register_message_handler(tariff_2, Text(equals='Тариф "С КУРАТОРОМ"', ignore_case=True))
    dp.register_message_handler(tariff_3, Text(equals='Тариф "С ЛЮСЕЙ"', ignore_case=True))
