import logging
import os


def setup_logging(log_file="log/mylog.log", log_level=logging.INFO):
    """Настраивает логирование с выводом в консоль и записью в файл."""

    # Создаем логгер
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Создаем обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Создаем обработчик для записи в файл
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))  # Создаем директорию, если ее нет

    file_handler = logging.FileHandler(log_file, 'w', encoding='utf-8')
    file_handler.setLevel(log_level)
    file_formatter = logging.Formatter(
        '[%(asctime)s] #%(levelname)-8s %(filename)s:'
        '%(lineno)d - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    class ErrorLogFilter(logging.Filter):
        def filter(self, record):
            return record.levelname == 'ERROR'

    formatter_1 = logging.Formatter(
        fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:'
            '%(lineno)d - %(message)s'
    )

    error_file = logging.FileHandler('log/error.log', 'a', encoding='utf-8')
    error_file.setLevel(logging.DEBUG)
    error_file.addFilter(ErrorLogFilter())
    error_file.setFormatter(formatter_1)
    logger.addHandler(error_file)

    return logger
