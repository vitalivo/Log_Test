from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def hello_world(request):
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')

    return HttpResponse('Hello, world!')