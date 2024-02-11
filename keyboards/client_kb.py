from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but1 = KeyboardButton('Подписка 1')
but2 = KeyboardButton('Подписка 2')
but3 = KeyboardButton('Подписка 3')

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

but6 = KeyboardButton('Лайвхак')

kb_client_6 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_6.add(but6)
