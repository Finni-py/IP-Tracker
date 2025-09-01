import sqlite3
from  app.utils.take_path import found_path


def take_user_history(user_id: str) -> list:
    # Возвращает список с запросами пользователя
    db = sqlite3.connect(found_path(), check_same_thread=False)
    cursor = db.cursor()

    cursor.execute('''
    SELECT user_request
    FROM request JOIN users_names ON request.user_id = users_names.id
    WHERE chat_id = ?''', (user_id,))

    rows = cursor.fetchall()
    db.close()

    lst_with_requests = [row[0] for row in rows]
    return lst_with_requests
