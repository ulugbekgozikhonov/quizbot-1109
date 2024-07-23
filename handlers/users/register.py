from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.user import phone_number_markup, remove_markup
from states.user import RegisterState
from loader import dp,dbmanager,bot
from utils.db_api.query import insert_user

@dp.callback_query_handler(state=RegisterState.language)
async def language_handler(call: types.CallbackQuery, state: FSMContext):
    language = call.data
    if language == "uz":
        await call.message.answer("Ism Familiyangizni kiriting.")
    elif language == "ru":
        await call.message.answer("Ведите ваше имя и фамилия")
    elif language == "en":
        await call.message.answer("Enter full name")
    await call.answer()
    await state.update_data(language=language)
    await RegisterState.full_name.set()

@dp.message_handler(state=RegisterState.full_name)
async def full_name_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    language = data['language']
    full_name = message.text
    await state.update_data(full_name=full_name)
    if language == "uz":
        await message.answer("Telefon raqamingizni yuboring. Tugmani bosing", reply_markup=phone_number_markup)
    elif language == "ru":
        await message.answer("Ведите свой номер", reply_markup=phone_number_markup)
    elif language == "en":
        await message.answer("Enter your phone number", reply_markup=phone_number_markup)
    await RegisterState.phone_number.set()

@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def phone_number_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    
    phone_number = message.contact.phone_number
    language = data['language']
    chat_id = data['chat_id']
    full_name = data['full_name']    
    response = dbmanager.insert_data(insert_sql=insert_user,data=(full_name,phone_number,chat_id,language))

    if response:
        if language == "uz":
            await message.answer("Siz registratsiya jarayonidan o'tdingiz", reply_markup=remove_markup)
        elif language == "ru":
            await message.answer("Вы успешно прошли регистратси", reply_markup=remove_markup)
        elif language == "en":
            await message.answer("You register succeffully", reply_markup=remove_markup)
    else:
        await bot.send_message(chat_id=909437832,text="Registratsiya jarayonida xatolik chiqdi")
    await state.finish()