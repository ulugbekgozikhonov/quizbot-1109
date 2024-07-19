from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext

from keyboards.inline.user import language_markup
from states.user import RegisterState
from loader import dp,dbmanager
from utils.db_api.query import get_user_by_chat_id


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    chat_id = message.chat.id
    dbmanager.connect()
    user = dbmanager.query_data_fetch_one(query_sql=get_user_by_chat_id,data=(chat_id,))
    dbmanager.close()
    if user:
        await message.answer("Welcome to quiz bot")
    else:
        await state.update_data(chat_id=chat_id)
        await message.answer(f"""
    Tilni tanlang!
    Выберите язык!
    Choose language!
    """, reply_markup=language_markup)
        await RegisterState.language.set()
