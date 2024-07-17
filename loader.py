from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.database import DatabaseManager
from data.config import *

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dbmanager = DatabaseManager(DB_NAME,DB_USER,DB_PASSWORD,DB_HOST,DB_PORT)