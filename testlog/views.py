from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def hello_world(request):
    logger.info('Hello, world!')
    return HttpResponse('Hello, world!')