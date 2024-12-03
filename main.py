from handlers.user_handlers import user_register
from handlers.admin_handlers import admin_register

import asyncio
from aiogram import Dispatcher, Bot


async def main():
    bot = Bot(token='TOKEN')
    dp = Dispatcher()

    admin_register(dp)
    user_register(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
