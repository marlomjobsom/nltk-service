#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SQLite 3 persistence initialization
"""

import os

from core.persistence import constant
from core.persistence.model.user_model import UserModel
from utils import path


def db_init():
    """ Initialize the production database """
    if not os.path.exists(path.DATABASE_FOLDER_PATH):
        os.mkdir(path.DATABASE_FOLDER_PATH)

    constant.DATABASE_INSTANCE.init(path.DATABASE_FILE_PATH)
    __init_tables()


def __init_tables():
    """ Create tables on database """
    if not UserModel.table_exists():
        UserModel.create_table()
