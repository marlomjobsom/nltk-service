#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Generic model class
"""

# pylint: disable=too-few-public-methods

import peewee

from core.persistence import constant


class GenericModel(peewee.Model):
    """
    Generic model class
    """
    class Meta:
        """
        Indicate in which database the model will be persisted
        """
        database = constant.DATABASE_INSTANCE
