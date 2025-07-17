# IP-Tracker Telegram Bot

👋 Добро пожаловать в IP-Tracker — Telegram-бот для получения информации по номеру телефона.

---

## Возможности

- 📱 Пробивка номера телефона: оператор, регион, возможные утечки  
- 🌐 Пробивка IP-адреса: геолокация, провайдер, подозрительная активность  
- Удобные команды: `/start`, `/help`, `/phone`, `/ip`   

---

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/yourusername/ip-tracker-bot.git
   cd ip-tracker-bot


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

* Python 3.x
* [pyTelegramBotAPI (telebot)](https://github.com/eternnoir/pyTelegramBotAPI)
* [phonenumbers](https://github.com/daviddrysdale/python-phonenumbers)
* python-dotenv

---

## Лицензия

MIT License
