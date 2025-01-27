from aiogram import Router
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData
# from aiogram.utils import executor

from service.CbRF import currency

# Инициализируем роутер уровня модуля
router = Router()

# Данные о валютах
currencies = currency()

# Параметры пагинации
ITEMS_PER_PAGE = 10

# Хранилище выбранных валют
selected_currencies = set()


# Функция для создания инлайн-клавиатуры с пагинацией
# def get_currency_keyboard(page: int = 0):
    # keyboard = InlineKeyboardMarkup(row_width=1)
    # start = page * ITEMS_PER_PAGE
    # end = start + ITEMS_PER_PAGE
    # for currency in currencies[start:end]:
    #     button_text = f"{currency['name']} ({currency['charCode']})"
    #     keyboard.add(InlineKeyboardButton(text=button_text, callback_data=button_text))
    #
    # # Кнопки навигации
    # navigation_buttons = []
    # if start > 0:
    #     navigation_buttons.append(InlineKeyboardButton(
    #         text='⬅️ Назад', callback_data=navigation_cb.new(page=page - 1, action='navigate')))
    # if end < len(currencies):
    #     navigation_buttons.append(InlineKeyboardButton(
    #         text='Вперед ➡️', callback_data=navigation_cb.new(page=page + 1, action='navigate')))
    #
    # if navigation_buttons:
    #     keyboard.row(*navigation_buttons)
    #
    # # Кнопка "ОК"
    # keyboard.add(InlineKeyboardButton(text='ОК', callback_data='finish'))

    # return keyboard


# # Обработчик команды /start
# @router.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer("Выберите валюты:", reply_markup=get_currency_keyboard())
#
#
# # Обработчик нажатий на кнопки валют
# @router.callback_query_handler(currency_cb.filter(action='select'))
# async def select_currency(callback_query: types.CallbackQuery, callback_data: dict):
#     currency_id = callback_data['id']
#     if currency_id in selected_currencies:
#         selected_currencies.remove(currency_id)
#         await callback_query.answer("Валюта удалена из выбранных.")
#     else:
#         selected_currencies.add(currency_id)
#         await callback_query.answer("Валюта добавлена в выбранные.")
#     await callback_query.message.edit_reply_markup(reply_markup=get_currency_keyboard())
#
#
# # Обработчик нажатий на кнопки навигации
# @router.callback_query_handler(navigation_cb.filter(action='navigate'))
# async def navigate(callback_query: types.CallbackQuery, callback_data: dict):
#     page = int(callback_data['page'])
#     await callback_query.message.edit_reply_markup(reply_markup=get_currency_keyboard(page=page))
#     await callback_query.answer()
#
#
# # Обработчик нажатия на кнопку "ОК"
# @router.callback_query_handler(text='finish')
# async def finish_selection(callback_query: types.CallbackQuery):
#     if selected_currencies:
#         selected_list = [currency for currency in currencies if currency['id'] in selected_currencies]
#         response = "Вы выбрали следующие валюты:\n"
#         response += "\n".join([f"{cur['name']} ({cur['charCode']})" for cur in selected_list])
#     else:
#         response = "Вы не выбрали ни одной валюты."
#     await callback_query.message.edit_text(response)
#     selected_currencies.clear()
#     await callback_query.answer()

