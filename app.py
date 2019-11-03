#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
REST API for NLTK functions
"""

import init

from utils import logger

# pylint: disable=invalid-name
flask_app_wrapper = init.setup()

# Runners
if __name__ == '__main__':
    logger.info('Running using Flask')
    flask_app_wrapper.run()

elif __name__ == 'uwsgi_file_app':
    # Set the WSGI 'application' variable callable to allow using uWSGI caller:
    # pylint: disable=invalid-name
    logger.info('Running using uWSGI')
    application = flask_app_wrapper.flask_app
