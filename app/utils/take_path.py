import os


def found_path() -> str:
    """
    Возвращает абсолютный путь к файлу базы данных (database.db),
    который хранится в корне проекта.
    """
    root_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
    db_path = os.path.join(root_dir, "database.db")

    return db_path
