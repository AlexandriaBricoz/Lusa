from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

but1 = KeyboardButton('Тариф "САМОСТОЯТЕЛЬНЫЙ"')
but2 = KeyboardButton('Тариф "С КУРАТОРОМ"')
but3 = KeyboardButton('Тариф "С ЛЮСЕЙ"')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but1).add(but2).add(but3)

but1 = KeyboardButton('👋 Привет')

kb_client_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_1.add(but1)

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
button_pay_1 = InlineKeyboardButton(text="Оплатить", callback_data="tariff_1",
                                    url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
button_pay_1_1 = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_1_1", )
# Добавляем кнопки на клавиатуру в виде списка
pay_1.add(button_pay_1).add(button_pay_1_1)

pay_2 = InlineKeyboardMarkup()

# Добавляем кнопки на клавиатуру
button_pay_2 = InlineKeyboardButton(text="Оплатить", callback_data="tariff_2",
                                    url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
button_pay_2_1 = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_2_1", )
# Добавляем кнопки на клавиатуру в виде списка
pay_2.add(button_pay_2).add(button_pay_2_1)

pay_3 = InlineKeyboardMarkup()

# Добавляем кнопки на клавиатуру
button_pay_3 = InlineKeyboardButton(text="Оплатить", callback_data="tariff_3",
                                    url='https://www.tinkoff.ru/rm/zhabina.lyudmila10/SrHII56565')
button_pay_3_1 = InlineKeyboardButton(text="Проверить оплату", callback_data="tariff_3_1", )
# Добавляем кнопки на клавиатуру в виде списка
pay_3.add(button_pay_3).add(button_pay_3_1)
