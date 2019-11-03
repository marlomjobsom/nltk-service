#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API for User entity
"""

from flask import request

from core.authentication import rest_auth_admin
from core.business.user_business import UserBusiness


class UserRest:
    """
    Rest API for User entity
    """

    @staticmethod
    @rest_auth_admin
    def create():
        """
        :return dict:
        :raises: UserEmptyNameException, UserAlreadyExistsException
        """
        user_name = request.data.decode()
        user_bean = UserBusiness.create(user_name)
        return user_bean.to_dict()

    @staticmethod
    @rest_auth_admin
    def read():
        """
        :return dict:
        :raise: UserDoesNotExistException
        """
        user_name = request.args.get('name')
        user_bean = UserBusiness.read(user_name)
        return user_bean.to_dict()

    @staticmethod
    @rest_auth_admin
    def delete():
        """
        :return int:
        :raise: UserDoesNotExistException
        """
        user_token = request.args.get('token')
        return UserBusiness.delete(user_token)
