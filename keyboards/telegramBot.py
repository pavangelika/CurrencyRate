from decimal import Decimal, ROUND_HALF_UP

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from service.CbRF import course_today


def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("1. Ежедневная рассылка курса", callback_data='daily')],
        [InlineKeyboardButton("2. Уведомление о каждом изменении курса", callback_data='change')],
        [InlineKeyboardButton("3. Уведомление при достижении курса USD", callback_data='usd_target')],
        [InlineKeyboardButton("4. Уведомление при достижении курса EUR", callback_data='eur_target')],
        [InlineKeyboardButton("5. Отписаться", callback_data='unsubscribe')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Выберите опцию:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    choice = query.data

    if choice == 'daily':
        # Логика для ежедневной рассылки
        query.edit_message_text(text="Вы подписаны на ежедневную рассылку курса валют.")
        # Сохранить подписку пользователя в базе данных или файле

    elif choice == 'change':
        # Логика для уведомлений при изменении курса
        query.edit_message_text(text="Вы подписаны на уведомления при изменении курса.")
        # Сохранить подписку пользователя

    elif choice == 'usd_target':
        # Запросить у пользователя целевой курс USD
        query.edit_message_text(text="Введите курс доллара для отслеживания (целое число):")
        return 'WAITING_FOR_USD_TARGET'

    elif choice == 'eur_target':
        # Запросить у пользователя целевой курс EUR
        query.edit_message_text(text="Введите курс евро для отслеживания (целое число):")
        return 'WAITING_FOR_EUR_TARGET'

    elif choice == 'unsubscribe':
        # Логика для отписки
        query.edit_message_text(text="Выберите, от каких уведомлений отписаться:")
        # Предоставить варианты отписки


def usd_target_input(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    try:
        target_value = int(user_input)
        # Сохранить целевое значение для пользователя
        update.message.reply_text(f"Вы установили уведомление при достижении курса доллара: {target_value} руб.")
    except ValueError:
        update.message.reply_text("Пожалуйста, введите целое число.")


def eur_target_input(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    try:
        target_value = int(user_input)
        # Сохранить целевое значение для пользователя
        update.message.reply_text(f"Вы установили уведомление при достижении курса евро: {target_value} руб.")
    except ValueError:
        update.message.reply_text("Пожалуйста, введите целое число.")


def check_and_notify(context: CallbackContext) -> None:
    data = course_today()
    usd_rate = Decimal(data['USD']).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    eur_rate = Decimal(data['EUR']).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    # Логика для отправки уведомлений подписанным пользователям
    # Например, проверка подписок в базе данных и отправка сообщений
