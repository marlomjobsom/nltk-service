#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Raised when try to create a user that already exists
"""


class UserAlreadyExistsException(Exception):
    """
    Raised when try to create a user that already exists
    """

    def __init__(self, name, *args, **kwargs):
        """
        :param str name:
        :param list args:
        :param dict kwargs:
        """
        super(UserAlreadyExistsException, self).__init__(
            'User "{}" already exists'.format(name), args, kwargs)
