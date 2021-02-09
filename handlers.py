# from loader import bot
# from config import admin_id
#
#
# async def send_to_admin(*args):
#     await bot.send_message(chat_id=admin_id, text="Бот запущен")


# @dp.message_handler(lambda message: 'Срок изготовления' == message.text)
# async def btn1(message: Message):
#     await message.reply('Все торты готовятся накануне, заказы принимаются не менее чем за 3 дня до доставки')
#
#
# @dp.message_handler(lambda message: 'Доставка' == message.text)
# async def btn1(message: Message):
#     await message.reply('Стоимость доставки по Москве - 500 руб., за МКАД +30 руб./км.')
#
#
# @dp.message_handler()
# async def keyboards(message: Message):
#     text = "Нажми на кнопку"
#     keyboards = ListOfButtons(text=['Смотреть каталог', 'Доставка', 'Срок изготовления'], align=[2, 1]).reply_keyboard
#
#     await message.reply(text=text, reply_markup=keyboards)
