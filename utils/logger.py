#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Logger """

import logging

logging.basicConfig(
    format='%(levelname)s:%(asctime)s:%(funcName)s:%(message)s', level=logging.INFO)

# pylint: disable=invalid-name
info = logging.info
warning = logging.warning
