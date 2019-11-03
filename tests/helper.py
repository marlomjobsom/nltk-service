#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Methods to help on unit tests
"""

import os
import unittest

from werkzeug.datastructures import Headers

import app
from core.persistence import database
from utils import path


class DataBaseTestCase(unittest.TestCase):

    def setUp(self):
        super(DataBaseTestCase, self).setUp()
        if os.path.exists(path.DATABASE_FILE_PATH):
            os.remove(path.DATABASE_FILE_PATH)

        database.db_init()

    def tearDown(self):
        super(DataBaseTestCase, self).tearDown()
        os.remove(path.DATABASE_FILE_PATH)


class RestTestCase(DataBaseTestCase):

    def setUp(self):
        super(RestTestCase, self).setUp()
        self.auth_header = self.build_auth_header('ca36c915cfb4ead0baa441f514f2983e')
        self.flask_test_client = app.flask_app_wrapper.test_client()

    @staticmethod
    def build_auth_header(token):
        headers = Headers()
        headers.add('Authorization', 'Bearer {}'.format(token))
        return headers


class NltkRestTestCase(RestTestCase):

    def setUp(self):
        super(NltkRestTestCase, self).setUp()
        response = self.flask_test_client.post(
            '/admin/token', data='nltk', headers=self.auth_header)
        self.nltk_auth_header = NltkRestTestCase.build_auth_header(response.json.get('token'))
