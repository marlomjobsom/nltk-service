#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Raised when try to read a user that doesn't exist
"""


class UserDoesNotExistException(Exception):
    """
    Raised when try to read a user that doesn't exist
    """

    def __init__(self, *args, name=None, token=None, **kwargs):
        """
        :param str name:
        :param str token:
        :param list args:
        :param dict kwargs:
        """
        msg = None

        if name:
            msg = 'User "{}" doesn\'t exist'.format(name)

        elif name == '':
            msg = 'Empty user name given'

        elif token:
            msg = 'User for token "{}" doesn\'t exist'.format(token)

        elif token == '':
            msg = 'Empty user token given'

        elif not name or not token:
            msg = 'Any argument given'

        super(UserDoesNotExistException, self).__init__(msg, args, kwargs)
