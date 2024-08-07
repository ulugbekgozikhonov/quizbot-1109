from aiogram import executor

from loader import dp,dbmanager
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.query import create_user_table,create_category_table,create_questions_table , create_answers_table,create_user_answers_table



async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    # dbmanager.create_table(create_table_sql=create_user_table)
    # dbmanager.create_table(create_table_sql=create_category_table)
    # dbmanager.create_table(create_answers_table)
    dbmanager.create_table(create_user_answers_table)
    await on_startup_notify(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup,skip_updates=True)
