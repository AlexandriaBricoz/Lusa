from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but1 = KeyboardButton('Тариф 1 « самостоятельной» 14 490₽')
but2 = KeyboardButton('Тариф 2 « с куратором» 23 490₽')
but3 = KeyboardButton('Тариф 3 « с Люсей» 35 490₽')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but1).add(but2).insert(but3)

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
