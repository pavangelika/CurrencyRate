import os
import json

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
print(CURRENCY)


LEXICON_NOTIFICATION_SEND: dict[str, str] = {
    'everyday_true': 'Вы подписаны на ежедневную рассылку курса валют',
    'everyday_false': 'Вы отписались от ежедневной рассылки курса',
    'exchange_rate_true': 'Вы подписаны на рассылку об изменении курса валют',
    'exchange_rate_false': 'Вы отписались от рассылки об изменении курса валют',
}


LEXICON_BTN: dict[str, str] = {
    'start_1': 'Выбор валюты',
    'start_2': 'Изменить валюту',
    'start_3': 'Ежедневная рассылка курса',
    'start_4': 'Уведомление об изменении курса',
    'start_5': 'Уведомление при достижении курса',
    'start_6': 'Посмотреть график',
    'start_7': 'Конвертер валют',
    'start_8': 'Курс валют в банках по гео',
    'start_9': 'Отписаться',

}

LEXICON_GLOBAL: list[dict[str,str]]= [
    {
        "command" : "start",
        "name": "Начало работы",
        "btn": "Выбор валюты",
        "text": "👋 Привет! Этот бот поможет вам следить за изменениями на валютном рынке.\n\n"
              "Возможности бота:\n\n"
              "📩 Ежедневная рассылка — получайте актуальные курсы валют каждый день.\n\n"
              "🔔 Уведомление об изменении курса — будьте в курсе любых изменений курса в реальном времени.\n\n"
              "🎯 Уведомление при достижении курса — настройте оповещения при достижении определенного значения курса.\n\n"
              "📈 Посмотреть график — анализируйте динамику курса с помощью наглядных графиков.\n\n"
              "Пожалуйста, выберите валюту для отслеживания, используя кнопку ниже ⬇️",
    },
    {
        "command" : "select_rate",
        "name": "Изменить валюту",
        "btn": "Изменить валюту",
        "notification_true": "Вы выбрали:",
        "notification_false": "Вы не выбрали валюту!"
    },
    {
        "command" : "today",
        "name": "Курс ЦБ сегодня",
        "btn": "Курс ЦБ сегодня",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command" : "everyday",
        "name": "Подписаться/Отписаться на ежедневную рассылку курса",
        "btn1": "Подписаться на ежедневную рассылку курса",
        "btn2": "Отписаться от ежедневной рассылки курса",
        "notification_true": "Вы подписаны на ежедневную рассылку курса валют",
        "notification_false": "Вы отписались от ежедневной рассылки курса"
    },
    {
        "command" : "exchange_rate",
        "name": "Подписаться/Отписаться на рассылку об изменении курса",
        "btn1": "Подписаться на рассылку об изменении курса",
        "btn2": "Отписаться от рассылки об изменении курса",
        "notification_true": "Вы подписаны на рассылку об изменении курса валют",
        "notification_false": "Вы отписались от рассылки об изменении курса валют"
    },
    {
        "command" : "chart",
        "name": "Посмотреть график",
        "btn1": "График на телефоне",
        "btn2": "График на ПК",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command" : "converter",
        "name": "Конвертер валют",
        "btn": "Конвертер валют",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command" : "in_banks",
        "name": "Курс валют в банках",
        "btn1": "Ввести гео",
        "btn2": "Показать банки",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command" : "user_remind",
        "name": "Напоминание о чем-то через заданный интервал времени",
        "btn1": "Отписаться от ежедневной рассылки ",
        "btn2": "Отписаться от рассылки изменений",
        "notification_true": "",
        "notification_false": ""
    },
    {
        "command" : "unsubscribe",
        "name": "Отписаться",
        "btn1": "",
        "btn2": "",
        "notification_true": "",
        "notification_false": ""
    }
    ]



