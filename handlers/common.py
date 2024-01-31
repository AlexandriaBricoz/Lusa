from aiogram import types
from collections import defaultdict
from create_bot import bot, client_commands, Dispatcher

old_message = defaultdict(bool)


# @dp.message_handler() # Фильтрация спама и мата в чате клиентской части
async def clean_chat(message: types.Message):
    if (message.text not in client_commands):
        await message.delete()
        await bot.send_message(message.from_user.id,
                               'Бот Вас не понял, пожалуйста воспользуйтесь командами на клавиатуре')
    old_message[message.from_user.id] = False


def register_common_handlers(dp: Dispatcher):
    dp.register_message_handler(clean_chat)
