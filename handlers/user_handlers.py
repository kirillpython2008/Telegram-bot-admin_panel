import sqlite3
from basedata.basedata import add_users, return_list_id_users

from aiogram import Dispatcher, types
from aiogram.filters import Command


async def start(message: types.Message):
    if message.from_user.id not in await return_list_id_users():
        await add_users(int(message.from_user.id))
        await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                         "я буду повторять за вам все ваши сообщения\n"
                         "(вообще я нужен для демонстрации работы админ панели)")
    else:
        await message.answer(f"Здравствуйте, {message.from_user.first_name}\n"
                         "я буду повторять за вам все ваши сообщения\n"
                         "(вообще я нужен для демонстрации работы админ панели)")
    

async def send_copy(message: types.Message):
    if type(message.text) == str:
        await message.answer(message.text)
    else:
        await message.answer("Напишите текст")
    

def user_register(dp: Dispatcher):
    dp.message.register(start, Command('start'))

    dp.message.register(send_copy)
