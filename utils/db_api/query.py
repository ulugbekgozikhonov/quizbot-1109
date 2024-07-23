create_user_table = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(55),
    phone_number VARCHAR(31) UNIQUE,
    chat_id BIGINT UNIQUE NOT NULL,
    lang VARCHAR(3) NOT NULL DEFAULT 'en'
    )"""
    
insert_user = "INSERT INTO users(full_name,phone_number,chat_id,lang) VALUES(%s,%s,%s,%s)"

get_user_by_chat_id = "SELECT * FROM users WHERE chat_id=%s"

create_category_table = """CREATE TABLE IF NOT EXISTS categories(
    id SERIAL PRIMARY KEY,
    title_uz VARCHAR(55),
    title_ru VARCHAR(55),
    title_en VARCHAR(55)
    )"""

insert_category = """INSERT INTO categories(title_uz,title_ru,title_en) VALUES(%s,%s,%s)"""

get_all_categories = "SELECT * FROM categories"