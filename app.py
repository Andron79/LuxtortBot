# from loader import bot, dp
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
# #from handlers import dp, send_to_admin
# import config
#
# async def on_shutdown(dp):
#     await bot.close()
#
#
# async def send_to_admin(*args):
#     await bot.send_message(chat_id=config.admin_id, text="Бот запущен")
#
#
# def main():
#     #from handlers import dp, send_to_admin
#     executor.start_polling(dp, on_startup=send_to_admin)
#
#     #executor.start_polling(dp, on_shutdown=on_shutdown)
#
#
# if __name__ == '__main__':
#     main()


# from loader import bot, dp
#
#
# async def on_shutdown(dp):
#     await bot.close()
#
#
# if __name__ == '__main__':
#     from aiogram import executor
#     from handlers import dp
#
#     executor.start_polling(dp, on_shutdown=on_shutdown)


from loader import bot


async def on_shutdown(dp):
    await bot.close()


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown)