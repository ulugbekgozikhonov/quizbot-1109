from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from loader import dbmanager
from utils.db_api.query import get_all_categories,get_answers

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
            
def start_quiz(lang):
    reply_mrkup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    if lang=="uz":
        start = KeyboardButton("🔰Boshlash")
        back = KeyboardButton("⬅️Orqaga")
    elif lang == "ru":
        start = KeyboardButton("🔰Начать")
        back = KeyboardButton("⬅️Назад")
    elif lang == "en":
        start = KeyboardButton("🔰Start")
        back = KeyboardButton("⬅️Back")
        
    return reply_mrkup.add(start,back)


def answers(lang,question_id):
    answers = dbmanager.query_data_fetch_all(get_answers,(question_id,))
    answer_murkup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    for answer in answers:
        if lang == "uz":
            btn = KeyboardButton(answer[1])
        elif lang == "ru":
            btn = KeyboardButton(answer[2])
        elif lang == "en":
            btn = KeyboardButton(answer[3])
        answer_murkup.add(btn)
    
    return answer_murkup
    