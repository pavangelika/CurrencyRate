import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))  # Директория, где находится lexicon.py
file_path = os.path.join(current_dir, "../save_files/currency_code.json")


def create_buttons_from_json_file(file_path):
    # Чтение данных из файла
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # Создание словаря CURRENCY
    CURRENCY = {}
    for i, item in enumerate(json_data, start=1):
        button_key = f'cur_{i}'
        button_value = f"{item['name']} ({item['charCode']})"
        CURRENCY[button_key] = button_value
    return CURRENCY


CURRENCY = create_buttons_from_json_file(file_path)

LEXICON_MENU: list[dict[str, str]] = [
    {"command": "start", "name": "Сброс всех параметров. Начать заново"},
    {"command": "menu", "name": "Действия с ботом"},
    {"command": "user_remind","name": "Напоминание о чем-то через заданный интервал времени"}
]

LEXICON_IN_MESSAGE: list[dict[str, str]] = [
    {"command": "select_rate", "btn": "Изменить валюту"},
    {"command": "today", "btn": "Курс ЦБ сегодня"},
    {"command": "everyday", "btn1": "Подписаться на ежедневную рассылку курса",
     "btn2": "Отписаться от ежедневной рассылки курса"},
    {"command": "chart", "btn": "Посмотреть график"},
    {"command": "in_banks", "btn": "Курс валют в банках"},
]

LEXICON_GLOBAL: list[dict[str, str]] = [
    {
        "command": "start",
        "name": "Сброс всех параметров. Начать заново",
        "btn": "Выбор валюты",
        "text": "👋 Привет! Этот бот поможет вам следить за изменениями на валютном рынке.\n\n"
                "Возможности бота:\n\n"
                "📩 Ежедневная рассылка — получайте актуальны курс валют ЦБ каждый день.\n\n"
                "🔔 Уведомление об изменении курса — будьте в курсе любых изменений курса в реальном времени.\n\n"
                "🎯 Уведомление при достижении курса — настройте оповещения при достижении определенного значения курса.\n\n"
                "📈 Посмотреть график — анализируйте динамику курса с помощью наглядных графиков.\n\n"
                "Пожалуйста, выберите валюту для отслеживания, используя кнопку ниже ⬇️",
    },
    {
        "command": "select_rate",
        "name": "Изменить валюту",
        "btn": "Изменить валюту",
        "notification_true": "Выбранная валюта:",
        "notification_false": "Вы не выбрали валюту!"
    },
    {
        "command": "today",
        "name": "Курс ЦБ сегодня",
        "btn": "Курс ЦБ сегодня"
    },
    {
        "command": "everyday",
        "name": "Подписаться/Отписаться на ежедневную рассылку курса",
        "btn1": "Подписаться на ежедневную рассылку курса",
        "btn2": "Отписаться от ежедневной рассылки курса",
        "notification_true": "Вы подписаны на ежедневную рассылку курса валют",
        "notification_false": "Вы отписались от ежедневной рассылки курса"
    },
    {
        "command": "exchange_rate",
        "name": "Подписаться/Отписаться на рассылку курса следующего дня",
        "btn1": "Подписаться на рассылку курса следующего дня",
        "btn2": "Отписаться от рассылки курса следующего дня",
        "notification_true": "Вы подписаны на рассылку курса валют следующего дня",
        "notification_false": "Вы отписались от рассылки курса валют следующего дня"
    },
    {
        "command": "chart",
        "name": "Посмотреть график",
        "btn1": "График на телефоне",
        "btn2": "График на ПК",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command": "converter",
        "name": "Конвертер валют",
        "btn": "Конвертер валют",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command": "in_banks",
        "name": "Курс валют в банках моего города",
        "btn1": "Отправить геопозицию",
        "btn2": "Показать банки",
        "notification_true": "",
        "notification_false": ""
    }
]

LEXICON_BTN: dict[str, str] = {
    'start_1': 'Выбор валюты',
    'start_2': 'Изменить валюту'

}
