#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Database instantiation unit tests
"""

import os
import sqlite3
import unittest

from core.persistence import database
from utils import path


class DataBaseTestCase(unittest.TestCase):

    def tearDown(self):
        if os.path.exists(path.DATABASE_FILE_PATH):
            os.remove(path.DATABASE_FILE_PATH)

    def test_db_init(self):
        database.db_init()
        self.assertTrue(os.path.exists(path.DATABASE_FILE_PATH))

    def test_usermodel_schema_creation(self):
        sql = 'SELECT SQL FROM sqlite_master WHERE TYPE = "table" AND name = "usermodel"'
        database.db_init()
        connection = sqlite3.connect(path.DATABASE_FILE_PATH)
        output = connection.execute(sql).fetchall()[0][0]
        self.assertIn('usermodel', output)


if __name__ == '__main__':
    unittest.main()
