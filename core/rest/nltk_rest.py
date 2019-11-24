#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API for NLTK functionalities
"""

from flask import request

from core.authentication import rest_auth_nltk
from core.business.nltk_business import NltkBusiness


class NltkRest:
    """
    API for NLTK functionalities
    """

    @staticmethod
    @rest_auth_nltk
    def words_tokenize():
        """ Return a tokenized copy of text, using NLTK’s recommended word tokenizer
        :return str: The texts tokenized form
        """
        texts_content = request.data
        return NltkBusiness.words_tokenize(texts_content)

    @staticmethod
    @rest_auth_nltk
    def pos_tags():
        """ Using NLTK's part of speech recommendation, returns a list of tagged tokens.
        :return str: the tagged tokens
        """
        tokens_content = request.data
        return NltkBusiness.pos_tags(tokens_content)

    @staticmethod
    @rest_auth_nltk
    def ne_chunks():
        """ Using NLTK's named entity chunker, returns a list of chunked tagged tokens.
        :return str: The tagged tokens chunked
        """
        tagged_tokens_content = request.data
        return NltkBusiness.ne_chunks(tagged_tokens_content)

    @staticmethod
    @rest_auth_nltk
    def words_snowball_stemmer():
        """ Stem an English words and return the stemmed form.
        :return str: The words stemmed form
        """
        words = request.data
        return NltkBusiness.words_snowball_stemmer(words)

    @staticmethod
    @rest_auth_nltk
    def words_lemmatize():
        """ Lemmatizes an English words and return the lemma form.
        :return str: The words lemma form
        """
        words = request.data
        return NltkBusiness.lemmatize(words)
