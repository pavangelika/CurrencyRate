from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

from service.CbRF import course_today, dinamic_course, parse_xml_data, graf_all_years_in_one

# Инициализируем роутер уровня модуля
router = Router()

# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(text=LEXICON_RU['/start'])
#
# @dp.message(Command(commands='help'))
# async def process_help_command(message: Message):
#     await message.answer(text=LEXICON_RU['/help'])
#
# @dp.message()
# async def send_echo(message: Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.reply(text=LEXICON_RU['no_echo'])


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        'Здесь должнен быть выбор функций: курс сегодня(выбор валют), график(выбор лет и валют), подписка на рассылку(ежедневная, на изменения, по достижении курса, отписка)')


@router.message(Command(commands=["today"]))
async def process_start_command(message: Message):
    await message.answer(course_today())


@router.message(Command(commands=["graf"]))
async def process_start_command(message: Message):
    dollarCod = 'R01235'
    dollar = dinamic_course(dollarCod)
    dollar_data = parse_xml_data(dollar)
    await message.answer(graf_all_years_in_one(dollar_data))


# Этот хэндлер будет срабатывать на команду "/help"
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Тут пока ничего нет'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
# @dp.message()
# async def send_echo(message: Message):
#     await message.reply(text=message.text)

# Этот хэндлер будет срабатывать на тип контента "photo"
@router.message(F.content_type == ContentType.PHOTO)
async def process_send_photo(message: Message):
    await message.reply(text='Вы прислали фото')


# Этот хэндлер будет срабатывать на тип контента "photo"
@router.message(F.content_type == ContentType.VOICE)
async def process_send_photo(message: Message):
    await message.reply(text='Вы прислали звук')


# Этот хэндлер будет срабатывать на тип контента "photo"
@router.message(F.content_type == ContentType.VIDEO)
async def process_send_photo(message: Message):
    await message.reply(text='Вы прислали видео')


