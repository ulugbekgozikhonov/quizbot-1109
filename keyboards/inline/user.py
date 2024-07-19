from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
language_markup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        ],
        [
            InlineKeyboardButton(text="🇺🇸 English", callback_data="en")
        ]
    ]
)