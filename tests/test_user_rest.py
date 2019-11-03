#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
UserRest unit tests
"""

import unittest

from tests.helper import RestTestCase
from utils import mime_types


class UserRestCreateTestCase(RestTestCase):

    def setUp(self):
        super(UserRestCreateTestCase, self).setUp()
        self.url = '/admin/token'
        self.data = 'UserRestCreateTestCase'

    def test_create_status_ok(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertEqual(200, response.status_code)

    def test_create_content_type(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_create_content_has_name(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertIn('name', response.json.keys())

    def test_create_content_has_token(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertIn('token', response.json.keys())

    def test_create_content_name(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertEqual(self.data, response.json.get('name'))

    def test_create_content_token_str(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertIsInstance(response.json.get('token'), str)

    def test_create_content_token_len(self):
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertTrue(len(response.json.get('token')) > 0)

    def test_create_existing_user_status_code(self):
        self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertEqual(400, response.status_code)

    def test_create_existing_user_content_type(self):
        self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_create_existing_user_content_has_error(self):
        self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertIn('error', response.json.keys())

    def test_create_existing_user_content_error(self):
        self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.assertEqual('User "{}" already exists'.format(self.data), response.json.get('error'))

    def test_create_empty_user_name(self):
        response = self.flask_test_client.post(self.url, headers=self.auth_header)
        self.assertEqual(400, response.status_code)

    def test_create_empty_user_name_content_has_error(self):
        response = self.flask_test_client.post(self.url, headers=self.auth_header)
        self.assertIn('error', response.json.keys())

    def test_create_empty_user_name_content_error(self):
        response = self.flask_test_client.post(self.url, headers=self.auth_header)
        self.assertEqual('User name given is an empty string', response.json.get('error'))

    def test_create_no_auth_status_code(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(401, response.status_code)

    def test_create_no_auth_content(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


class UserRestReadTestCase(RestTestCase):

    def setUp(self):
        super(UserRestReadTestCase, self).setUp()
        self.url = '/admin/token?name='
        self.data = 'UserRestReadTestCase'
        self.non_existing_user = 'UserRestReadTestCaseNonExisting'
        self.url_get_existing_user = ''.join([self.url, self.data])
        self.url_get_non_existing_user = ''.join([self.url, self.non_existing_user])
        self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)

    def test_read_status_ok(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertEqual(200, response.status_code)

    def test_read_content_type(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_read_content_has_name(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertIn('name', response.json.keys())

    def test_read_content_has_token(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertIn('token', response.json.keys())

    def test_read_content_name(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertEqual(self.data, response.json.get('name'))

    def test_read_content_token_str(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertIsInstance(response.json.get('token'), str)

    def test_read_content_token_len(self):
        response = self.flask_test_client.get(self.url_get_existing_user, headers=self.auth_header)
        self.assertTrue(len(response.json.get('token')) > 0)
    
    def test_read_existing_user_status_code(self):
        response = self.flask_test_client.get(
            self.url_get_non_existing_user, headers=self.auth_header)
        self.assertEqual(400, response.status_code)

    def test_read_existing_user_content_type(self):
        response = self.flask_test_client.get(
            self.url_get_non_existing_user, headers=self.auth_header)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_read_existing_user_content_has_error(self):
        response = self.flask_test_client.get(
            self.url_get_non_existing_user, headers=self.auth_header)
        self.assertIn('error', response.json.keys())

    def test_read_existing_user_content_error(self):
        response = self.flask_test_client.get(
            self.url_get_non_existing_user, headers=self.auth_header)
        self.assertEqual(
            'User "{}" doesn\'t exist'.format(self.non_existing_user), response.json.get('error'))
    
    def test_read_empty_user_name(self):
        response = self.flask_test_client.get(self.url, headers=self.auth_header)
        self.assertEqual(400, response.status_code)

    def test_read_empty_user_name_content_type(self):
        response = self.flask_test_client.get(self.url, headers=self.auth_header)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_read_empty_user_name_content_has_error(self):
        response = self.flask_test_client.get(self.url, headers=self.auth_header)
        self.assertIn('error', response.json.keys())

    def test_read_empty_user_name_content_error(self):
        response = self.flask_test_client.get(self.url, headers=self.auth_header)
        self.assertEqual('Empty user name given', response.json.get('error'))

    def test_read_no_auth_status_code(self):
        response = self.flask_test_client.get(self.url)
        self.assertEqual(401, response.status_code)

    def test_read_no_auth_content(self):
        response = self.flask_test_client.get(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


class UserRestDeleteTestCase(RestTestCase):

    def setUp(self):
        super(UserRestDeleteTestCase, self).setUp()
        self.url = '/admin/token?token='
        self.data = 'UserRestDeleteTestCase'
        self.non_existing_token = '12345'

        response = self.flask_test_client.post(self.url, data=self.data, headers=self.auth_header)
        self.token = response.json.get('token')
        self.delete_url = ''.join([self.url, self.token])
        self.delete_non_existing_token_url = ''.join([self.url, self.non_existing_token])

    def test_delete_status_ok(self):
        response = self.flask_test_client.delete(self.delete_url, headers=self.auth_header)
        self.assertTrue(200, response.status_code)

    def test_delete_content_type(self):
        response = self.flask_test_client.delete(self.delete_url, headers=self.auth_header)
        self.assertTrue(mime_types.APPLICATION_JSON, response.content_type)

    def test_delete_content_row(self):
        response = self.flask_test_client.delete(self.delete_url, headers=self.auth_header)
        self.assertEqual(1, response.json)

    def test_delete_existing_user_content_has_error(self):
        response = self.flask_test_client.delete(
            self.delete_non_existing_token_url, headers=self.auth_header)
        self.assertIn('error', response.json.keys())

    def test_delete_non_existing_token(self):
        response = self.flask_test_client.delete(
            self.delete_non_existing_token_url, headers=self.auth_header)
        self.assertEqual(
            'User for token "{}" doesn\'t exist'.format(self.non_existing_token),
            response.json.get('error'))
    
    def test_delete_empty_user_name(self):
        response = self.flask_test_client.delete(self.url, headers=self.auth_header)
        self.assertEqual(400, response.status_code)

    def test_delete_empty_user_name_content_type(self):
        response = self.flask_test_client.delete(self.url, headers=self.auth_header)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_delete_empty_user_name_content_has_error(self):
        response = self.flask_test_client.delete(self.url, headers=self.auth_header)
        self.assertIn('error', response.json.keys())

    def test_delete_empty_user_name_content_error(self):
        response = self.flask_test_client.delete(self.url, headers=self.auth_header)
        self.assertEqual('Empty user token given', response.json.get('error'))

    def test_delete_no_auth_status_code(self):
        response = self.flask_test_client.delete(self.url)
        self.assertEqual(401, response.status_code)

    def test_delete_no_auth_content(self):
        response = self.flask_test_client.delete(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


if __name__ == '__main__':
    unittest.main()
