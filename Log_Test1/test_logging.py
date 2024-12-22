import logging

logger = logging.getLogger('django')

logger_request = logging.getLogger('django.request')
logger_security = logging.getLogger('django.security')


def generate_logs():
    print("=== Генерация сообщений логгирования ===")

    logger.debug("Debug message from django logger")
    logger.info("Info message from django logger")
    logger.warning("Warning message from django logger")
    logger.error("Error message from django logger")
    logger.critical("Critical message from django logger")
    logger_request.error("Request error message from django.request logger")

    logger_security.warning("Security warning message from django.security logger")
    logger_security.error("Security error message from django.security logger")

    print("=== Сообщения логгирования сгенерированы ===")


if __name__ == "__main__":
    generate_logs()
