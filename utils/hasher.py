#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Generate hashes """

import hashlib
import time

UTF_8 = 'utf-8'


def build_md5(text=''):
    """ Builds MD5 hash
    :param str text: text to mix with the hash generation
    """
    timestamp = time.time()
    hash_input = '{text}{timestamp}'.format(text=text, timestamp=timestamp)
    encoded_hash_input = hash_input.encode(UTF_8)

    md5_hash = hashlib.md5()
    md5_hash.update(encoded_hash_input)

    return md5_hash.hexdigest()
