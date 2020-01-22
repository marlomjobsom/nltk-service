#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Flask app wrapper
"""

import flask

from core.exceptions.not_authenticated_request_exception import NotAuthenticatedRequestException


class FlaskAppWrapper:
    """
    Flask app wrapper
    """

    def __init__(self, name, port):
        """
        :param str name: the application name
        :param int port: the port of the webserver
        """
        self.__port = port
        self.__app = flask.Flask(import_name=name)

    @property
    def flask_app(self):
        """ It returns a Flask instance to uWSGI execute it
        :return flask.Flask:
        """
        return self.__app

    def test_client(self):
        """ Creates a test client for this application
        :return flask.testing.FlaskClient:
        """
        return self.__app.test_client()

    def run(self):
        """
        Runs the application on a local development server.
        Do not use run() in a production setting! Use uWSGI instead
        """
        self.__app.run(port=self.__port, debug=True)

    def add_post_endpoint(self, words, endpoint_handler):
        """ Register a new POST end-point to the web-server
        :param list words: the words that will compose the URL address
        :param func endpoint_handler: the function that will handle the request
        """
        self.__add_endpoint(method='POST', words=words, endpoint_handler=endpoint_handler)

    def add_get_endpoint(self, words, endpoint_handler):
        """ Register a new POST end-point to the web-server
        :param list words: the words that will compose the URL address
        :param func endpoint_handler: the function that will handle the request
        """
        self.__add_endpoint(method='GET', words=words, endpoint_handler=endpoint_handler)

    def add_delete_endpoint(self, words, endpoint_handler):
        """ Register a new POST end-point to the webserver
        :param list words: the words that will compose the URL address
        :param func endpoint_handler: the function that will handle the request
        """
        self.__add_endpoint(method='DELETE', words=words, endpoint_handler=endpoint_handler)

    def __add_endpoint(self, method, words, endpoint_handler):
        """ Register a new end-point to the web-server
        :param str method: the request method (e.g: GET, POST, ...)
        :param list words: the words that will compose the URL address
        :param func endpoint_handler: the function that will handle the request
        """
        self.__app.add_url_rule(
            rule=FlaskAppWrapper.__build_url(words),
            endpoint=endpoint_handler.__name__,
            view_func=_EndpointHandler(endpoint_handler),
            methods=[method])

    @staticmethod
    def __build_url(words):
        """
        :param list words: the words that will compose the URL address
        :return str: a URL address
        """
        separator = '/'

        for index, word in enumerate(words):
            if word.startswith(separator):
                words[index] = word[1:]

            elif word.endswith(separator):
                words[index] = word[:-1]

        return separator + separator.join(words)


class _EndpointHandler:
    """ Handles the end-point call """

    # pylint: disable=too-few-public-methods

    def __init__(self, endpoint_handler):
        """
        :param func endpoint_handler:
        """
        self.__endpoint_handler = endpoint_handler

    def __call__(self, *args, **kwargs):
        """ Executes the end-point handler and wraps its return content into JSON
        :param list args:
        :param dict kwargs:
        :return flask.Response: the JSON response content
        """
        response = None

        try:
            output = self.__endpoint_handler(*args, **kwargs)
            response = flask.jsonify(output)

        except NotAuthenticatedRequestException:
            response = flask.Response('<h1>Authentication Required!</h1>', 401)

        except Exception as err:
            msg = err.args[0]
            response = flask.jsonify(dict(error=msg))
            response.status_code = 400

        return response
