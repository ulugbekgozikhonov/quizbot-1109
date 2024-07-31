from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.user import language_markup
from keyboards.default.user import start_quiz,categories,answers
from states.user import QuizState
from loader import dp,dbmanager
from utils.db_api.query import get_user_by_chat_id,get_quiestions_by_category_name,insert_user_answers

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
        question_list = dbmanager.query_data_fetch_all(get_quiestions_by_category_name,(category_name,category_name,category_name))
        questions_tuple = question_list[0]
        await state.update_data(question_index=1)
        await state.update_data(question_list=question_list)
        question_id = questions_tuple[0]
        await state.update_data(question_id=question_id)
        answer_markup,answer_ids = answers(lang,question_id)
        await state.update_data(answer_ids=answer_ids)
        
        if lang == "uz":
            await message.answer(text=f"{questions_tuple[1]}",reply_markup=answer_markup)
        elif lang == "ru":
            await message.answer(text=f"{questions_tuple[2]}",reply_markup=answer_markup)
        elif lang == "en":
            await message.answer(text=f"{questions_tuple[3]}",reply_markup=answer_markup)
        await QuizState.answer.set()
        
    elif text.startswith("⬅️"):
        await QuizState.category.set()
        await message.answer(text="⬅️",reply_markup=categories(lang))    
    
@dp.message_handler(state=QuizState.answer)
async def get_answer_handler(message:types.Message,state:FSMContext):
    user_answer = message.text
    chat_id = message.chat.id
    data = await state.get_data()
    answer_ids: dict = data.get('answer_ids')
    answer_id = 0
    question_id = data.get('question_id')

    for key,value in answer_ids.items():
        if value == user_answer:
            answer_id = key
            break
    if answer_id == 0:
        await message.answer("Error Text")
    is_correct = True if answer_id == answer_ids["correct_id"] else False
    dbmanager.insert_data(insert_user_answers,(chat_id,question_id,answer_id,is_correct))
    
    lang = data.get("lang")
    question_list = data.get('question_list')
    question_index = data.get('question_index')
    
    if question_index == len(question_list):
        await message.answer("Natijalar",reply_markup=ReplyKeyboardRemove())
        await state.finish()
    
    questions_tuple = question_list[question_index]
    question_id = questions_tuple[0]
    await state.update_data(question_id=question_id)
    answer_markup,answer_ids = answers(lang,question_id)
    await state.update_data(answer_ids=answer_ids)
    
    if lang == "uz":
        await message.answer(text=f"{questions_tuple[1]}",reply_markup=answer_markup)
    elif lang == "ru":
        await message.answer(text=f"{questions_tuple[2]}",reply_markup=answer_markup)
    elif lang == "en":
        await message.answer(text=f"{questions_tuple[3]}",reply_markup=answer_markup)
    question_index+=1
    await state.update_data(question_index=question_index)
    await QuizState.answer.set()
    

    
    
    
    
    
    
    