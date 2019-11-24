#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API for NLTK functionalities
"""

from core import nltk_wrapper


class NltkBusiness:
    """
    API for NLTK functionalities
    """
    ENGLISH_LANG = 'english'

    @staticmethod
    def words_tokenize(texts_content):
        """ Return a tokenized copy of text, using NLTK’s recommended word tokenizer
        :param str texts_content: Texts in JSON with key pointing to a text.
                                  e.g: {doc1: text1, doc2: text2, ...}
        :return dict: The texts tokenized form
        """
        return nltk_wrapper.words_tokenize(
            texts_content, language=NltkBusiness.ENGLISH_LANG)

    @staticmethod
    def pos_tags(tokens_content):
        """ Using NLTK's part of speech recommendation, returns a list of tagged tokens.
        :param str tokens_content: Tokens in JSON with key pointing to a list of tokens.
                                    e.g: {key1: [token1, token2], key2: [token3, token4], ...}
        :return dict: the tagged tokens
        """
        return nltk_wrapper.pos_tags(tokens_content)

    @staticmethod
    def ne_chunks(tagged_tokens_content):
        """ Using NLTK's named entity chunker, returns a list of chunked tagged tokens.
        :param str tagged_tokens_content: Tags in JSON with key pointing to a list of tagged tokens.
                                           e.g: {key1: [[token1, tag1], [token2, tag2]], ...}
        :return dict: The tagged tokens chunked
        """
        return nltk_wrapper.ne_chunks(tagged_tokens_content)

    @staticmethod
    def words_snowball_stemmer(words):
        """ Stem an English words and return the stemmed form.
        :param str words: The words in JSON that are stemmed.
                          e.g: {text1: [word1, word2, ...], ...}
        :return dict: The words stemmed form
        """
        return nltk_wrapper.words_snowball_stemmer(
            words, ignore_stopwords=False, language=NltkBusiness.ENGLISH_LANG)

    @staticmethod
    def lemmatize(words):
        """ Using NLTK's lemmatizer recommendation, returns a list of tagged tokens.
                :param str tokens_content: Tokens in JSON with key pointing to a list of tokens.
                                            e.g: {key1: [token1, token2], key2: [token3, token4], ...}
                :return dict: the tagged tokens
                """
        return nltk_wrapper.lemmatize(words)
