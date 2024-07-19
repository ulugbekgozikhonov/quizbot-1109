from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

remove_markup = ReplyKeyboardRemove()

phone_number_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share contact", request_contact=True)
        ]
    ],resize_keyboard=True
)