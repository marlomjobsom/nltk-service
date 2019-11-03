#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Represents the table "usermodel"
"""

import peewee

from core.persistence.model.abstract_model import GenericModel


class UserModel(GenericModel):
    """
    Represents the table "usermodel"
    """
    id = peewee.IntegerField(primary_key=True)
    name = peewee.CharField(unique=True, null=False, constraints=[peewee.Check('name <> ""')])
    token = peewee.CharField(unique=True, null=False, constraints=[peewee.Check('token <> ""')])
