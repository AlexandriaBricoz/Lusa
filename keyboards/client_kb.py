from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

but1 = KeyboardButton('Тариф 1 « самостоятельной» 14 490₽')
but2 = KeyboardButton('Тариф 2 « с куратором» 23 490₽')
but3 = KeyboardButton('Тариф 3 « с Люсей» 35 490₽')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but1).add(but2).add(but3)

but1 = KeyboardButton('👋 Привет')

kb_client_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_1.add(but1)

but3 = KeyboardButton('📹 Смотреть видео')

kb_client_3 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_3.add(but3)

but5 = KeyboardButton('💼 Познакомиться с тарифами')

kb_client_5 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_5.add(but5)

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
