#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialize the application
"""

import argparse

from core import settings
from core.flask_app_wrapper import FlaskAppWrapper
from core.persistence import database
from core.rest.nltk_rest import NltkRest
from core.rest.user_rest import UserRest

APP_NAME = 'NLTK service'
DESCRIPTION = 'Service that provides a REST access to NLTK functionalities'
HELP_MSG_PORT = 'Port where the server will be listen'
HELP_ADMIN_TOKEN = 'Authenticate the boot and allow REST for CRUD tokens'


def setup():
    """ Setup the environment to run the webserver
    :return core.flask_app_wrapper.FlaskAppWrapper: a flask app wrapper instance
    """
    args = __get_args()
    __init_database()
    __set_admin_token(args.admin_token)
    return __get_flask_app_wrapper(args.port)


def __get_flask_app_wrapper(port):
    """
    :param int port: the webserver port
    :return core.flask_app_wrapper.FlaskAppWrapper: a flask app wrapper instance
    """
    flask_app_wrapper = FlaskAppWrapper(name=APP_NAME, port=port)
    __set_admin_end_points(flask_app_wrapper)
    __set_nltk_end_points(flask_app_wrapper)
    return flask_app_wrapper


def __set_nltk_end_points(flask_app_wrapper):
    """ Sets the end-points for NLTK
    :param core.flask_app_wrapper.FlaskAppWrapper flask_app_wrapper: a flask app wrapper instance
    """
    flask_app_wrapper.add_post_endpoint(['words_tokenize'], NltkRest.words_tokenize)
    flask_app_wrapper.add_post_endpoint(['words_snowball_stemmer'], NltkRest.words_snowball_stemmer)
    flask_app_wrapper.add_post_endpoint(['lemmatize'], NltkRest.lemmatize)
    flask_app_wrapper.add_post_endpoint(['pos_tags'], NltkRest.pos_tags)
    flask_app_wrapper.add_post_endpoint(['ne_chunks'], NltkRest.ne_chunks)


def __set_admin_end_points(flask_app_wrapper):
    """ Sets the end-points for Admin users to manage users tokens
    :param core.flask_app_wrapper.FlaskAppWrapper flask_app_wrapper: a flask app wrapper instance
    """
    flask_app_wrapper.add_post_endpoint(['admin', 'token'], UserRest.create)
    flask_app_wrapper.add_get_endpoint(['admin', 'token'], UserRest.read)
    flask_app_wrapper.add_delete_endpoint(['admin', 'token'], UserRest.delete)


def __get_args():
    """
    :return argparse.Namespace: the arguments from CLI interface
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)

    parser.add_argument(
        '--port', type=int, help=HELP_MSG_PORT, default=settings.DEFAULT_PORT)
    parser.add_argument(
        '--admin_token', type=str, help=HELP_ADMIN_TOKEN, default=settings.DEFAULT_ADMIN_USER_TOKEN)

    args, _ = parser.parse_known_args()

    return args


def __init_database():
    """ Initializes the database"""
    database.db_init()


def __set_admin_token(admin_token):
    """
    :param str admin_token:
    """
    settings.ADMIN_USER_TOKEN = admin_token
