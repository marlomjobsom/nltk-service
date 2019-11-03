#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Raised when try to create a user using a empty string name
"""


class UserEmptyNameException(Exception):
    """
    Raised when try to create a user using a empty string name
    """

    def __init__(self, *args, **kwargs):
        """
        :param list args:
        :param dict kwargs:
        """
        super(UserEmptyNameException, self).__init__(
            'User name given is an empty string', args, kwargs)
