import sqlite3
from app.utils.take_path import found_path


# Подключаемся к базе данных (создается, если не существует)
db = sqlite3.connect(found_path(), check_same_thread=False)
cursor = db.cursor()

# Создаем таблицу пользователей, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS users_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT,
    chat_id TEXT NOT NULL
)
''')

# Создаем таблицу с запросами пользователей, если она еще не создана
cursor.execute('''
CREATE TABLE IF NOT EXISTS request (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    user_request TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users_names (id)
)
''')

db.commit()
