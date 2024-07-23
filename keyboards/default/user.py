from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loader import dbmanager
from utils.db_api.query import get_all_categories

remove_markup = ReplyKeyboardRemove()

phone_number_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Share contact", request_contact=True)
        ]
    ],resize_keyboard=True
)

def categories(lang):
    categoris_btn = ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
    categories_db = dbmanager.query_data_fetch_all(get_all_categories)
    index = 1 if lang == "uz" else 2 if lang == "ru" else 3 if lang == "en" else None
    
    for category in categories_db:
       categoris_btn.insert(KeyboardButton(category[index]))
    
    return categoris_btn
            
start_quiz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Start")
        ],
        [
            KeyboardButton("⬅️")
        ]
    ]
)    