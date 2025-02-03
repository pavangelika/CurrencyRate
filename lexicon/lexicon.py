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
# print(CURRENCY)


LEXICON_TEXT: dict[str, str] = {
    'start': "👋 Привет! Этот бот поможет вам следить за изменениями на валютном рынке.\n\n"
              "Возможности бота:\n\n"
              "📩 Ежедневная рассылка — получайте актуальные курсы валют каждый день.\n\n"
              "🔔 Уведомление об изменении курса — будьте в курсе любых изменений курса в реальном времени.\n\n"
              "🎯 Уведомление при достижении курса — настройте оповещения при достижении определенного значения курса.\n\n"
              "📈 Посмотреть график — анализируйте динамику курса с помощью наглядных графиков.\n\n"
              "Пожалуйста, выберите валюту для отслеживания, используя кнопку ниже ⬇️",
}

LEXICON_NOTIFICATION_SEND: dict[str, str] = {
    'everyday_true': 'Вы подписаны на ежедневную рассылку курса валют',
    'everyday_false': 'Вы отписались от ежедневной рассылки курса',
    'exchange_rate_true': 'Вы подписаны на рассылку об изменении курса валют',
    'exchange_rate_false': 'Вы отписались от рассылки об изменении курса валют',
}

LEXICON_COMMANDS_MENU: dict[str, str] = {
    '/start': 'Начало работы',
    '/select_rate': 'Выбор валюты',
    '/today': 'Курс сегодня',
    '/everyday': 'Подписаться/Отписаться на ежедневную рассылку курса',
    '/exchange_rate': 'Подписаться/Отписаться на рассылку об изменении курса',
    '/chart': 'Посмотреть график',
    '/user_remind': 'Напоминание о чем-то через заданный интервал времени'

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



