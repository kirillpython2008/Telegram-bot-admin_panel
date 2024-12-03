from button.inline_button import admin_inline_keyboard
from admin_state import admin_state
from basedata.basedata import return_count_users
from basedata.basedata import return_list_id_users

from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


async def admin_panel(message: types.Message):
    if message.from_user.id == 5119363066:
        await message.answer("Здравствуйте, товарищ админ, что прикажете ?",
                             reply_markup=admin_inline_keyboard)
    else:
        await message.answer("Вы не админ")


async def count_users(query: types.CallbackQuery):
    await query.message.answer("бота запустили\n"
                               f"{await return_count_users()} пользователей")
    

async def sending_mess_1(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("Введите сообщение для рассылки")
    await state.set_state(admin_state.admin_panel.sending_message)


async def sending_mess_2(message: types.Message, state: FSMContext):
    for i in await return_list_id_users():
        try:
            await message.answer(id=i, text=message.text)
        except:
            continue
    await state.clear()


def admin_register(dp: Dispatcher):
    dp.message.register(admin_panel, Command('admin'))

    dp.callback_query.register(count_users, F.data == 'count_users')

    dp.callback_query.register(sending_mess_1, F.data == 'sending')

    dp.message.register(sending_mess_2, admin_state.admin_panel.sending_message)
