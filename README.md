# IP-Tracker Telegram Bot

👋 Добро пожаловать в IP-Tracker — Telegram-бот для получения информации по номеру телефона и ip-адресу.

---

## Возможности

- 📱 Пробивка номера телефона: оператор, страна, город.
- 🌐 Пробивка IP-адреса: геолокация, провайдер, точка на карте, страна, город.
- Сохранение истории всех запросов в SQL базе данных.
- Удобные команды: `/start`, `/help`, `/phone`, `/ip`   

---

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/finniy/IP-Tracker.git
   cd IP-Tracker


2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` и добавьте в него ваш API ключ Telegram:

   ```
   API_KEY=ваш_токен_бота
   ```

4. Запустите бота:

   ```bash
   python bot.py
   ```

---

## Использование

* `/start` — Приветствие и описание возможностей
* `/help` — Список доступных команд
* `/phone` — Запрос информации по номеру телефона
* `/ip` — Запрос информации по ip-адресу

---

## Технологии

* Python 3.8+
* [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)
* [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
* python-dotenv

---

## Лицензия

MIT License
