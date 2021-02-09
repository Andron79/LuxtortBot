# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
#
# menu = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text='Каталог тортов'),
#          ],
#         [KeyboardButton(text='Доставка'),
#          KeyboardButton(text='Начинки')
#          ],
#     ],
#     resize_keyboard=True
# )


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Детские торты"),
        ],
        [
            KeyboardButton(text="На День Рождения "),
            KeyboardButton(text="Без мастики")
        ],
    ],
    resize_keyboard=True
)