#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UserBusiness unit tests
"""

import unittest

from core.business.user_business import UserBusiness
from core.persistence.bean.user_bean import UserBean
from core.persistence.exception.user_already_exists_exception import UserAlreadyExistsException
from core.persistence.exception.user_does_not_exist_exception import UserDoesNotExistException
from tests.helper import DataBaseTestCase


class UserBusinessCreateTestCase(DataBaseTestCase):

    def setUp(self):
        super(UserBusinessCreateTestCase, self).setUp()
        self.user_name = 'UserBusinessCreateTestCase'

    def test_create(self):
        user_bean = UserBusiness.create(self.user_name)
        self.assertIsInstance(user_bean, UserBean)

    def test_create_user_already_exists(self):
        with self.assertRaises(UserAlreadyExistsException) as context:
            UserBusiness.create(self.user_name)
            UserBusiness.create(self.user_name)

        self.assertIsInstance(context.exception, UserAlreadyExistsException)


class UserBusinessReadTestCase(DataBaseTestCase):

    def setUp(self):
        super(UserBusinessReadTestCase, self).setUp()
        self.user_name = 'UserBusinessReadTestCase'
        UserBusiness.create(self.user_name)

    def test_read(self):
        user_bean = UserBusiness.read(self.user_name)
        self.assertIsInstance(user_bean, UserBean)

    def test_read_nonexistent_user(self):
        with self.assertRaises(UserDoesNotExistException) as context:
            UserBusiness.read(None)

        self.assertIsInstance(context.exception, UserDoesNotExistException)


class UserBusinessDeleteTestCase(DataBaseTestCase):

    def setUp(self):
        super(UserBusinessDeleteTestCase, self).setUp()
        self.user_bean = UserBusiness.create('UserBusinessDeleteTestCase')

    def test_delete(self):
        row_affected = UserBusiness.delete(self.user_bean.token)
        self.assertEqual(1, row_affected)

    def test_delete_nonexistent_user(self):
        with self.assertRaises(UserDoesNotExistException) as context:
            UserBusiness.delete(None)

        self.assertTrue(context.exception, UserDoesNotExistException)


if __name__ == '__main__':
    unittest.main()
