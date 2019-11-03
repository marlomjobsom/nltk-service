#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UserDAO unit tests
"""

import sqlite3
import unittest

import peewee

from core.persistence.dao.user_dao import UserDAO
from core.persistence.exception.user_already_exists_exception import UserAlreadyExistsException
from core.persistence.exception.user_does_not_exist_exception import UserDoesNotExistException
from core.persistence.exception.user_empty_name_exception import UserEmptyNameException
from tests.helper import DataBaseTestCase


class UserDAOCreateTestCase(DataBaseTestCase):

    def setUp(self):
        super(UserDAOCreateTestCase, self).setUp()
        self.user_dao = UserDAO()
        self.user_name = 'UserDAOCreateTestCase'

    def test_create_has_primary_key(self):
        user_bean = self.user_dao.create(name=self.user_name)
        self.assertIsNotNone(user_bean.primary_key)

    def test_create_has_token(self):
        user_bean = self.user_dao.create(name=self.user_name)
        self.assertIsNotNone(user_bean.token)

    def test_create_equal_name(self):
        user_bean = self.user_dao.create(name=self.user_name)
        self.assertEqual(user_bean.name, self.user_name)

    def test_create_duplicate(self):
        expected = (UserAlreadyExistsException, peewee.IntegrityError, sqlite3.IntegrityError)

        with self.assertRaises(expected_exception=expected) as context:
            self.user_dao.create(name=self.user_name)
            self.user_dao.create(name=self.user_name)

        self.assertIsInstance(context.exception, UserAlreadyExistsException)

    def test_create_with_empty_string_name(self):
        expected = (UserEmptyNameException, peewee.IntegrityError, sqlite3.IntegrityError)

        with self.assertRaises(expected_exception=expected) as context:
            self.user_dao.create(name='')

        self.assertIsInstance(context.exception, UserEmptyNameException)


class UserDAOReadTestCase(DataBaseTestCase):

    def setUp(self):
        super(UserDAOReadTestCase, self).setUp()
        self.user_dao = UserDAO()
        self.user_bean = self.user_dao.create(name='UserDAOReadTestCase')

    def test_read_to_dict_equal_name(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        user_bean_dict = user_bean_read.to_dict()
        self.assertEqual(self.user_bean.name, user_bean_dict.get('name'))

    def test_read_to_dict_equal_token(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        user_bean_dict = user_bean_read.to_dict()
        self.assertEqual(self.user_bean.token, user_bean_dict.get('token'))

    def test_read_has_primary_key(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        self.assertTrue(user_bean_read.primary_key)

    def test_read_equal_name(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        self.assertEqual(self.user_bean.name, user_bean_read.name)

    def test_read_token_is_true(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        self.assertEqual(self.user_bean.token, user_bean_read.token)

    def test_read_by_token_has_primary_key(self):
        user_bean_read = self.user_dao.read_by_token(token=self.user_bean.token)
        self.assertTrue(user_bean_read.primary_key)

    def test_read_by_token_equal_name(self):
        user_bean_read = self.user_dao.read_by_token(token=self.user_bean.token)
        self.assertEqual(self.user_bean.name, user_bean_read.name)

    def test_read_by_token_equal(self):
        user_bean_read = self.user_dao.read_by_token(token=self.user_bean.token)
        self.assertEqual(self.user_bean.token, user_bean_read.token)

    def test_read_equal_obj(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        self.assertEqual(self.user_bean, user_bean_read)

    def test_read_not_equal_obj(self):
        user_bean_read = self.user_dao.read(name=self.user_bean.name)
        user_bean_read.name = None
        self.assertNotEqual(self.user_bean, user_bean_read)

    def test_read_non_existing_user(self):
        with self.assertRaises(UserDoesNotExistException):
            self.user_dao.read('test_read_non_existing_user')

    def test_read_input_false(self):
        with self.assertRaises(UserDoesNotExistException):
            self.user_dao.read(False)

    def test_read_input_none(self):
        with self.assertRaises(UserDoesNotExistException):
            self.user_dao.read(None)

    def test_read_by_token_non_existing_user(self):
        with self.assertRaises(UserDoesNotExistException):
            self.user_dao.read_by_token('test_read_non_existing_user')


class UserDAODeleteTestCase(DataBaseTestCase):

    def setUp(self):
        super(UserDAODeleteTestCase, self).setUp()
        self.user_dao = UserDAO()
        user_name = 'UserDAODeleteTest'
        self.user_dao.create(name=user_name)
        self.user_bean = self.user_dao.read(name=user_name)

    def test_delete_row_affected(self):
        row = self.user_dao.delete(self.user_bean)
        self.assertEqual(1, row)

    def test_delete_non_existing_row_affected(self):
        self.user_dao.delete(self.user_bean)
        row = self.user_dao.delete(self.user_bean)
        self.assertEqual(0, row)


if __name__ == '__main__':
    unittest.main()
