from aiogram.dispatcher.filters.state import StatesGroup, State

class RegisterState(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()

class QuizState(StatesGroup):
    category = State()
    start_or_back = State()
    answer = State()
    question = State()