#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NLTK wrapper unit test
"""

import json
import unittest

from nltk import Tree

from core import nltk_wrapper


class NltkWrapperTestCase(unittest.TestCase):

    def setUp(self):
        super(NltkWrapperTestCase, self).setUp()
        self.text = 'It brings libraries coverage as well'
        self.text_word_list = ['It', 'brings', 'libraries', 'coverage', 'as', 'well']

        self.text_words_list = {'DOC1': self.text_word_list, 'DOC2': self.text_word_list}
        self.json_text = {'DOC1': self.text, 'DOC2': self.text}

        self.first_tagged_tokens = [('Now', 'RB'), ('for', 'IN'), ('anything', 'NN')]
        self.second_tagged_tokens = [
            ('And', 'CC'), ('now', 'RB'), ('for', 'IN'), ('something', 'NN'), ('different', 'JJ')]

        self.first_tags_list = ['Now', 'for', 'anything']
        self.second_tags_list = ['And', 'now', 'for', 'something', 'different']
        self.tagged_tokens_list = {
            'DOC1': self.first_tagged_tokens, 'DOC2': self.second_tagged_tokens}

        self.json_tags = {'DOC1': self.first_tags_list, 'DOC2': self.second_tags_list}
        self.expected_dict = {'S': [['NNP', 'Hello'], ['NN', 'World']]}

        self.chunk_tree = Tree('S', [['NNP', 'Hello'], ['NN', 'World']])
        self.expected_chunked_response = {
            "DOC1": {
                "S": [
                    ["Now", "RB"], ["for", "IN"], ["anything", "NN"]
                ]
            },
            "DOC2": {
                "S": [
                    ["And", "CC"], ["now", "RB"], ["for", "IN"],
                    ["something", "NN"], ["different", "JJ"]
                ]
            }
        }

        self.words = {'DOC1': ['brings', 'libraries', 'coverage']}
        self.stemmed_words = {'DOC1': ['bring', 'librari', 'coverag']}

    def test_words_tokenize(self):
        texts_tokenized = nltk_wrapper.words_tokenize(json.dumps(self.json_text))
        self.assertEqual(self.text_words_list, texts_tokenized)

    def test_post_tags(self):
        tagged_tokens = nltk_wrapper.pos_tags(json.dumps(self.json_tags))
        self.assertEqual(self.tagged_tokens_list, tagged_tokens)

    def test_ne_chunks(self):
        chunked_tagged_tokens = nltk_wrapper.ne_chunks(json.dumps(self.tagged_tokens_list))
        self.assertEqual(self.expected_chunked_response, chunked_tagged_tokens)

    def test_words_snowball_stemmer(self):
        output = nltk_wrapper.words_snowball_stemmer(json.dumps(self.words))
        self.assertEqual(self.stemmed_words, output)


if __name__ == '__main__':
    unittest.main()
