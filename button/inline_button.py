from aiogram import types

admin_inline_kb = [[types.InlineKeyboardButton(text='Пользователи', callback_data='count_users'),
                    types.InlineKeyboardButton(text='Рассылка', callback_data='sending')]]

admin_inline_keyboard = types.InlineKeyboardMarkup(inline_keyboard=admin_inline_kb)
