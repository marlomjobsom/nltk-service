#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Paths for files and folders into the project
"""

import os

UTILS_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PROJECT_FOLDER_PATH = os.path.dirname(UTILS_FOLDER_PATH)
DATABASE_FOLDER_PATH = os.path.join(ROOT_PROJECT_FOLDER_PATH, 'database')
DATABASE_FILE_PATH = os.path.join(DATABASE_FOLDER_PATH, 'sqlite3.db')
