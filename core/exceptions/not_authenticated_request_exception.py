#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NotAuthenticatedRequestException(Exception):

    def __init__(self, response, *args, **kwargs):
        """
        :param flask.wrappers.Response response:
        :param list args:
        :param dict kwargs:
        """
        super(NotAuthenticatedRequestException, self).__init__(
            'Request not authorized: "{}"'.format(response), args, kwargs)
