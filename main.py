import asyncio

from aiogram import Bot, Dispatcher

from config_data import config
from handlers import user_handlers
from logging_settings import setup_logging
from service.CbRF import currency


# Функция конфигурирования и запуска бота
async def main():
    # Инициализируем бота
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)

    # Настраиваем логирование
    logger = setup_logging()
    logger.info('Starting bot')

    currency()

    try:
        # Пропускаем накопившиеся апдейты и запускаем polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)

    except asyncio.CancelledError:
        logger.info('Polling was cancelled')
    finally:
        # Закрываем сессию бота
        await bot.session.close()
        logger.info('Bot shutdown')


if __name__ == '__main__':
    asyncio.run(main())
