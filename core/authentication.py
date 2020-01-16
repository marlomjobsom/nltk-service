#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Validate requests
"""

import re
from functools import wraps

from core.exceptions.not_authenticated_request_exception import NotAuthenticatedRequestException

import flask

from core import settings
from core.business.user_business import UserBusiness
from core.persistence.exception.user_does_not_exist_exception import UserDoesNotExistException


def rest_auth_admin(method):
    """ Admin end-point authentication.
    :param function method: the method decorated
    :return func: the function that wrap the parameters of the method decorated
    """

    @wraps(method)
    def parameters():
        """
        :return function|flask.wrappers.Response:
        """
        if not __has_admin_token(flask.request):
            raise NotAuthenticatedRequestException(flask.request)

        return method()

    return parameters


def rest_auth_nltk(method):
    """ NLTK end-point authentication.
    :param function method: the method decorated
    :return func: the function that wrap the parameters of the method decorated
    """

    @wraps(method)
    def parameters(*args, **kwargs):
        """ Gets the parameters of the method decorated
        :param list args:
        :param dict kwargs:
        :return function|flask.wrappers.Response:
        """
        if not __has_user_token(flask.request):
            raise NotAuthenticatedRequestException(flask.request)

        return method(*args, **kwargs)

    return parameters


def __has_user_token(request):
    """
    :param flask.wrappers.Response request:
    :return bool:
    """
    token = __get_bearer_token(request)

    try:
        return bool(UserBusiness.read_by_token(token))
    except UserDoesNotExistException:
        pass


def __has_admin_token(request):
    """
    :param flask.wrappers.Response request:
    :return bool:
    """
    token = __get_bearer_token(request)
    return settings.ADMIN_USER_TOKEN == token


def __get_bearer_token(request):
    """
    :param flask.wrappers.Response request:
    :return str:
    """
    content = request.environ.get('HTTP_AUTHORIZATION')

    if content:
        result = re.match(r'Bearer (.*)', content)

        if result:
            return result.group(1)


def __build_ask_authentication_response():
    """
    :return flask.wrappers.Response:
    """
    return flask.Response(
        '<h1>Authentication Required!</h1>', 401)
