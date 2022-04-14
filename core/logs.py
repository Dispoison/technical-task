import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger_format = logging.Formatter('%(asctime)s - %(levelname)s - '
                                  '%(message)s', "%Y-%m-%d %H:%M:%S")

file_handler = logging.FileHandler('technical_task.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logger_format)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logger_format)
logger.addHandler(console_handler)
