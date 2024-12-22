import django
django.setup()
import logging

from django.test import TestCase


class LoggingTestCase(TestCase):
    def test_debug_logging(self):
        logger = logging.getLogger('django')
        logger.debug('This is a debug message')

        with open('general.log', 'r') as f:
            self.assertIn('This is a debug message', f.read())

    def test_error_logging(self):
        logger = logging.getLogger('django.request')
        try:
            raise Exception('Test error')
        except Exception as e:
            logger.error('Error occurred', exc_info=True)
        # Check if the message was written to the log file
        with open('errors.log', 'r') as f:
            self.assertIn('Error occurred', f.read())
