from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

but1 = KeyboardButton('Тариф "САМОСТОЯТЕЛЬНЫЙ"')
but2 = KeyboardButton('Тариф "С КУРАТОРОМ"')
but3 = KeyboardButton('Тариф "С ЛЮСЕЙ"')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but1).add(but2).add(but3)

but1 = KeyboardButton('👋 Привет')

kb_client_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_1.add(but1)

but_video_3 = KeyboardButton('Смотреть третий урок')

kb_client_video_3 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_video_3.add(but_video_3)

but2_11 = KeyboardButton('Лайфхак')

kb_client_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_2.add(but2_11)

but3 = KeyboardButton('📹 Смотреть видео')

kb_client_3 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_3.add(but3)

but6 = KeyboardButton('Лайфхак')

kb_client_6 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_6.add(but6)

but_next = KeyboardButton('Продолжить')

kb_client_next = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_next.add(but_next)

button_tg = InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/lusy_zhabina")

# Создаем клавиатуру и добавляем в нее кнопку
keyboard_tg = InlineKeyboardMarkup()
keyboard_tg.add(button_tg)

but_next = KeyboardButton('Продолжить')

kb_client_next = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_next.add(but_next)

kb_client_5 = InlineKeyboardMarkup()

# Добавляем кнопки на клавиатуру
button1 = InlineKeyboardButton(text="Ознакомиться с программой курса", callback_data="tariffs")

# Добавляем кнопки на клавиатуру в виде списка
kb_client_5.add(button1)

pay_1 = InlineKeyboardMarkup()

# Добавляем кнопки на клавиатуру
button_pay_1 = InlineKeyboardButton(text="Оплатить 14 490₽", callback_data="tariff_1",
                                    url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
button_pay_1_1 = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_1_1", )
# Добавляем кнопки на клавиатуру в виде списка
pay_1.add(button_pay_1).add(button_pay_1_1)

pay_2 = InlineKeyboardMarkup()

# Добавляем кнопки на клавиатуру
button_pay_2 = InlineKeyboardButton(text="Оплатить 23 490₽", callback_data="tariff_2",
                                    url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
button_pay_2_1 = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_2_1", )
# Добавляем кнопки на клавиатуру в виде списка
pay_2.add(button_pay_2).add(button_pay_2_1)

pay_3 = InlineKeyboardMarkup()

# Добавляем кнопки на клавиатуру
button_pay_3 = InlineKeyboardButton(text="Оплатить 35 490₽", callback_data="tariff_3",
                                    url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
button_pay_3_1 = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_3_1", )
# Добавляем кнопки на клавиатуру в виде списка
pay_3.add(button_pay_3).add(button_pay_3_1)

#####################################################################################################################


# Кнопки для выбора тарифа
tariff_button1 = InlineKeyboardButton(text="Тариф 'САМОСТОЯТЕЛЬНЫЙ'", callback_data="tariff_1")
tariff_button2 = InlineKeyboardButton(text="Тариф 'С КУРАТОРОМ'", callback_data="tariff_2")
tariff_button3 = InlineKeyboardButton(text="Тариф 'С ЛЮСЕЙ'", callback_data="tariff_3")

# Клавиатура для выбора тарифа
tariff_keyboard = InlineKeyboardMarkup()
tariff_keyboard.add(tariff_button1)
tariff_keyboard.add(tariff_button2)
tariff_keyboard.add(tariff_button3)

# Кнопка приветствия
greet_button = InlineKeyboardButton(text="👋 Привет", callback_data="greet")

# Клавиатура для приветствия
greet_keyboard = InlineKeyboardMarkup()
greet_keyboard.add(greet_button)

# Кнопка для просмотра третьего урока
watch_lesson_button = InlineKeyboardButton(text="Смотреть третий урок", callback_data="watch_lesson_3")

# Клавиатура для просмотра третьего урока
watch_lesson_keyboard = InlineKeyboardMarkup()
watch_lesson_keyboard.add(watch_lesson_button)

# Кнопка "Лайфхак"
lifehack_button = InlineKeyboardButton(text="Лайфхак", callback_data="lifehack")

# Клавиатура "Лайфхак"
lifehack_keyboard = InlineKeyboardMarkup()
lifehack_keyboard.add(lifehack_button)

# Кнопка для просмотра видео
watch_video_button = InlineKeyboardButton(text="📹 Смотреть видео", callback_data="watch_video")

# Клавиатура для просмотра видео
watch_video_keyboard = InlineKeyboardMarkup()
watch_video_keyboard.add(watch_video_button)

# Кнопка "Продолжить"
continue_button = InlineKeyboardButton(text="Продолжить", callback_data="continue")

# Клавиатура "Продолжить"
continue_keyboard = InlineKeyboardMarkup()
continue_keyboard.add(continue_button)

# Кнопка "Подписаться на канал"
subscribe_button = InlineKeyboardButton(text="Подписаться на канал", url="https://t.me/lusy_zhabina")

# Клавиатура "Подписаться на канал"
subscribe_keyboard = InlineKeyboardMarkup()
subscribe_keyboard.add(subscribe_button)

# Кнопка "Ознакомиться с программой курса"
program_button = InlineKeyboardButton(text="Ознакомиться с программой курса", callback_data="program")

# Клавиатура "Ознакомиться с программой курса"
program_keyboard = InlineKeyboardMarkup()
program_keyboard.add(program_button)

# Кнопки и клавиатуры для оплаты различных тарифов
payment_button1 = InlineKeyboardButton(text="Оплатить 14 490₽", callback_data="tariff_1_payment",
                                       url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
payment_button1_check = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_1_check_payment")
payment_keyboard1 = InlineKeyboardMarkup()
payment_keyboard1.add(payment_button1, payment_button1_check)

payment_button2 = InlineKeyboardButton(text="Оплатить 23 490₽", callback_data="tariff_2_payment",
                                       url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
payment_button2_check = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_2_check_payment")
payment_keyboard2 = InlineKeyboardMarkup()
payment_keyboard2.add(payment_button2, payment_button2_check)

payment_button3 = InlineKeyboardButton(text="Оплатить 35 490₽", callback_data="tariff_3_payment",
                                       url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
payment_button3_check = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_3_check_payment")
payment_keyboard3 = InlineKeyboardMarkup()
payment_keyboard3.add(payment_button3, payment_button3_check)
