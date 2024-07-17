create_user_table = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(55),
    phone_number VARCHAR(31) UNIQUE,
    chat_id INTEGER UNIQUE NOT NULL,
    language VARCHAR(3) NOT NULL DEFAULT 'eng'
    )"""
    
