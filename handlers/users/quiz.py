from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from keyboards.inline.user import language_markup
from keyboards.default.user import start_quiz
from states.user import QuizState
from loader import dp,dbmanager
from utils.db_api.query import get_user_by_chat_id

@dp.message_handler(state=QuizState.category)
async def category_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang = data.get("lang")
    if lang == "uz":
        await message.answer("Sizga 10ta savol beriladi boshlash uchun start tugmasini bosing!", reply_markup=start_quiz)
    elif lang == "ru":
        await message.answer("Вам дадут 10 вопросов чтоьы начать нажмите на кнопку Старт!", reply_markup=start_quiz)
    elif lang == "en":
        await message.answer("You will be asked 10 questions, click the start button to start!", reply_markup=start_quiz)