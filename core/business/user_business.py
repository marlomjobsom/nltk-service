#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Business logic layer for User entity
"""

from core.persistence.dao.user_dao import UserDAO


class UserBusiness:
    """
    Business logic layer for User entity
    """

    @classmethod
    def create(cls, name):
        """
        :param str name:
        :return core.persistence.bean.user_bean.UserBean:
        :raises: UserEmptyNameException, UserAlreadyExistsException
        """
        return UserDAO.create(name)

    @classmethod
    def read(cls, name):
        """
        :param str name:
        :return core.persistence.bean.user_bean.UserBean:
        :raise: UserDoesNotExistException
        """
        return UserDAO.read(name)

    @classmethod
    def read_by_token(cls, token):
        """
        :param str token:
        :return core.persistence.bean.user_bean.UserBean:
        :raise: UserDoesNotExistException
        """
        return UserDAO.read_by_token(token)

    @classmethod
    def delete(cls, token):
        """
        :param str token:
        :return int:
        :raise: UserDoesNotExistException
        """
        user_bean = UserDAO.read_by_token(token)
        return UserDAO.delete(user_bean)
