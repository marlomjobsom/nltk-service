#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NLTK wrapper
"""

import json

import nltk
from nltk.stem import WordNetLemmatizer


def words_tokenize(texts_content, language='english'):
    """ Return a tokenized copy of text, using NLTK’s recommended word tokenizer
    :param str texts_content: Texts in JSON with key pointing to a text.
                               e.g: {doc1: text1, doc2: text2, ...}
    :param str language: the model name in the Punkt corpus
    :return dict: The texts tokenized form
    """
    json_content = json.loads(texts_content)
    dict_response = dict()

    for item in json_content:
        dict_response[item] = nltk.word_tokenize(text=json_content[item], language=language)

    return dict_response


def pos_tags(tokens_content):
    """ Using NLTK's part of speech recommendation, returns a list of tagged tokens.
    :param str tokens_content: Tokens in JSON with key pointing to a list of tokens.
                                e.g: {key1: [token1, token2], key2: [token3, token4], ...}
    :return dict: the tagged tokens
    """
    json_content = json.loads(tokens_content)
    dict_response = dict()

    for item in json_content:
        dict_response[item] = nltk.pos_tag(tokens=json_content[item])

    return dict_response


def ne_chunks(tagged_tokens_content):
    """ Using NLTK's named entity chunker, returns a list of chunked tagged tokens.
    :param str tagged_tokens_content: Tags in JSON with key pointing to a list of tagged tokens.
                                       e.g: {key1: [[token1, tag1], [token2, tag2]], ...}
    :return dict: The tagged tokens chunked
    """
    json_content = json.loads(tagged_tokens_content)
    dict_response = dict()

    for item in json_content:
        dict_response[item] = __tree2dict(nltk.ne_chunk(tagged_tokens=json_content[item]))

    return dict_response


def words_snowball_stemmer(words, ignore_stopwords=False, language='english'):
    """ Stem an English words and return the stemmed form.
    :param str words: The words in JSON that are stemmed. e.g: {text1: [word1, word2, ...], ...}
    :param bool ignore_stopwords: If set to True, stopwords are not stemmed and returned unchanged.
    :param str language: The language whose a stemmer subclass is instantiated.
    :return dict: The words stemmed form
    """
    json_content = json.loads(words)
    dict_response = dict()

    stemmer = nltk.stem.snowball.SnowballStemmer(
        language=language, ignore_stopwords=ignore_stopwords)

    for key in json_content:
        words_list = json_content[key]
        stemmed_words_list = list()

        for word in words_list:
            stemmed_words_list.append(stemmer.stem(word=word))

        dict_response[key] = stemmed_words_list

    return dict_response


def lemmatize(words):
    """ Lemmatize an English sentence and return the lemmatized form.
    :param str words: The words in JSON that are stemmed. e.g: {text1: [word1, word2, ...], ...}
    :return dict: The words stemmed form
    """
    json_content = json.loads(words)
    dict_response = dict()

    lemmatizer = nltk.stem.WordNetLemmatizer()

    for key in json_content:
        words_list = json_content[key]
        stemmed_words_list = list()

        for word in words_list:
            stemmed_words_list.append(lemmatizer.lemmatize(word=word))

        dict_response[key] = stemmed_words_list

    return dict_response


def __tree2dict(tree):
    """ Converts NLTK's Tree to a dictionary representation
    :param nltk.Tree tree: NLTK Tree to be converted to dict
    :return dict:
    """
    return {tree.label(): [__tree2dict(t) if isinstance(t, nltk.Tree) else t for t in tree]}
