from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

but1 = KeyboardButton('Контакты')
but2 = KeyboardButton('Режим работы')
but3 = KeyboardButton('Тренировки')
but4 = KeyboardButton('Преподаватели')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(but1).add(but2).insert(but3).add(but4)

but1 = KeyboardButton('Привет')

kb_client_1 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_1.add(but1)

but1 = KeyboardButton('Далее')

kb_client_2 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_2.add(but1)

but1 = KeyboardButton('Смотреть видео')

kb_client_3 = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client_3.add(but1)