#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import unittest

from tests.helper import NltkRestTestCase
from utils import mime_types


class RequestWordsTokenizeTestCase(NltkRestTestCase):

    def setUp(self):
        super(RequestWordsTokenizeTestCase, self).setUp()
        self.url = '/words_tokenize'
        self.data = json.dumps({'DOC1': 'It brings libraries coverage as well'})
        self.expected_data = {'DOC1': ['It', 'brings', 'libraries', 'coverage', 'as', 'well']}

    def test_words_tokenize_status_ok(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_words_tokenize_content_type(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_words_tokenize_expected_content(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(self.expected_data, response.json)

    def test_words_tokenize_no_auth_status_code(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(401, response.status_code)

    def test_words_tokenize_no_auth_content(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


class RequestPosTagsTestCase(NltkRestTestCase):

    def setUp(self):
        super(RequestPosTagsTestCase, self).setUp()
        self.url = '/pos_tags'
        self.data = json.dumps({'DOC1': ['hello', 'world']})
        self.expected_data = {'DOC1': [['hello', 'NN'], ['world', 'NN']]}

    def test_pos_tags_status_ok(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_pos_tags_content_type(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_pos_tags_expected_content(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(self.expected_data, response.json)

    def test_pos_tags_no_auth_status_code(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(401, response.status_code)

    def test_pos_tags_no_auth_content(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


class RequestNeChunksTestCase(NltkRestTestCase):

    def setUp(self):
        super(RequestNeChunksTestCase, self).setUp()
        self.url = '/ne_chunks'
        self.data = json.dumps({'DOC1': [['NNP', 'hello'], ['NN', 'world']]})
        self.expected_data = {'DOC1': {'S': [['NNP', 'hello'], ['NN', 'world']]}}

    def test_ne_chunks_status_ok(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_ne_chunks_content_type(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_ne_chunks_expected_content(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(self.expected_data, response.json)

    def test_ne_chunks_no_auth_status_code(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(401, response.status_code)

    def test_ne_chunks_no_auth_content(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


class RequestWordsSnowballStemmerTestCase(NltkRestTestCase):

    def setUp(self):
        super(RequestWordsSnowballStemmerTestCase, self).setUp()
        self.url = '/words_snowball_stemmer'
        self.data = json.dumps({'DOC1': ['brings', 'libraries', 'coverage']})
        self.expected_data = {'DOC1': ['bring', 'librari', 'coverag']}

    def test_words_snowball_stemmer_status_ok(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(200, response.status_code)

    def test_words_snowball_stemmer_content_type(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(mime_types.APPLICATION_JSON, response.content_type)

    def test_words_snowball_stemmer_expected_content(self):
        response = self.flask_test_client.post(
            self.url, headers=self.nltk_auth_header, data=self.data)
        self.assertEqual(self.expected_data, response.json)

    def test_words_snowball_stemmer_no_auth_status_code(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(401, response.status_code)

    def test_words_snowball_stemmer_no_auth_content(self):
        response = self.flask_test_client.post(self.url)
        self.assertEqual(b'<h1>Authentication Required!</h1>', response.data)


if __name__ == '__main__':
    unittest.main()
