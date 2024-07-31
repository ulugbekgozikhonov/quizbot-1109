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

get_all_categories = "SELECT * FROM categories  "


create_questions_table = """CREATE TABLE IF NOT EXISTS questions(
    id SERIAL PRIMARY KEY,
    title_uz TEXT, 
    title_ru TEXT,
    title_en TEXT,
    category_id INTEGER
    )"""
    
get_quiestions_by_category_name = "SELECT q.id,q.title_uz,q.title_ru,q.title_en FROM questions as q JOIN categories as c ON c.id=q.category_id WHERE c.title_uz = %s OR c.title_ru = %s OR c.title_en = %s LIMIT 10 OFFSET 0"


create_answers_table = """CREATE TABLE IF NOT EXISTS answers(
    id SERIAL PRIMARY KEY,
    title_uz TEXT, 
    title_ru TEXT,
    title_en TEXT,
    question_id INTEGER,
    is_correct BOOLEAN DEFAULT FALSE
    )"""


get_answers = "SELECT * FROM answers WHERE question_id=%s"



create_user_answers_table = """CREATE TABLE IF NOT EXISTS user_answers(
    id SERIAL PRIMARY KEY,
    chat_id INTEGER,
    question_id INTEGER,
    answer_id INTEGER,
    deleted BOOLEAN DEFAULT FALSE,
    is_correct BOOLEAN DEFAULT FALSE
    )"""

insert_user_answers = "INSERT INTO user_answers(chat_id,question_id,answer_id,is_correct) VALUES(%s,%s,%s,%s)"