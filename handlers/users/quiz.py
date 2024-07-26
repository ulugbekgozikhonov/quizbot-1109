from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.user import language_markup
from keyboards.default.user import start_quiz,categories,answers
from states.user import QuizState
from loader import dp,dbmanager
from utils.db_api.query import get_user_by_chat_id,get_quiestions_by_category_name

def get_text_by_lang(lang):
    if lang == "uz":
        return "Sizga 10ta savol beriladi boshlash uchun start tugmasini bosing!"
    elif lang == "ru":
        return "Вам дадут 10 вопросов чтоьы начать нажмите на кнопку Старт!"
    elif lang == "en":
        return "You will be asked 10 questions, click the start button to start!"
  

@dp.message_handler(state=QuizState.category)
async def category_handler(message: types.Message, state: FSMContext):
    category_name = message.text
    await state.update_data(category_name=category_name)
    data = await state.get_data()
    lang = data.get("lang")
    text = get_text_by_lang(lang)
    await message.answer(text=text,reply_markup=start_quiz(lang))
    await QuizState.start_or_back.set()
    

@dp.message_handler(state=QuizState.start_or_back)
async def start_or_back_handler(message:types.Message,state:FSMContext):
    data = await state.get_data()
    lang = data.get("lang")
    text = message.text
    if text.startswith("🔰"):
        category_name = data.get("category_name")
        questions_list = dbmanager.query_data_fetch_all(get_quiestions_by_category_name,(category_name,category_name,category_name))
        questions_tuple = questions_list[0]
        question_id = questions_tuple[0]
        if lang == "uz":
            await message.answer(text=f"{questions_tuple[1]}",reply_markup=answers(lang,question_id))
        elif lang == "ru":
            await message.answer(text=f"{questions_tuple[2]}",reply_markup=answers(lang,question_id))
        elif lang == "en":
            await message.answer(text=f"{questions_tuple[3]}",reply_markup=answers(lang,question_id))
        await QuizState.question.set()
    elif text.startswith("⬅️"):
        await QuizState.category.set()
        await message.answer(text="⬅️",reply_markup=categories(lang))    
    