#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
User DAO
"""

import peewee

from core.persistence.bean.user_bean import UserBean
from core.persistence.exception.user_already_exists_exception import UserAlreadyExistsException
from core.persistence.exception.user_does_not_exist_exception import UserDoesNotExistException
from core.persistence.exception.user_empty_name_exception import UserEmptyNameException
from core.persistence.model.user_model import UserModel
from utils import hasher


class UserDAO:
    """
    User DAO
    """

    @classmethod
    def create(cls, name):
        """
        :param str name:
        :return UserBean:
        :raises: UserEmptyNameException, UserAlreadyExistsException
        """
        md5_hash = hasher.build_md5(name)

        try:
            user_model_instance = UserModel.create(name=name, token=md5_hash)
            return UserBean(user_model_instance)
        except peewee.IntegrityError as err:
            msg = err.args[0]

            if 'CHECK' in msg:
                raise UserEmptyNameException()

            if 'UNIQUE' in msg:
                raise UserAlreadyExistsException(name)

    @classmethod
    def read(cls, name):
        """
        :param str name:
        :return UserBean:
        :raises: UserDoesNotExistException
        """
        try:
            return UserBean(UserModel.get(name=name))
        except UserModel.DoesNotExist:
            raise UserDoesNotExistException(name=name)

    @classmethod
    def read_by_token(cls, token):
        """
        :param str token:
        :return UserBean:
        :raises: UserDoesNotExistException
        """
        try:
            return UserBean(UserModel.get(token=token))
        except UserModel.DoesNotExist:
            raise UserDoesNotExistException(token=token)

    @classmethod
    def delete(cls, user_bean):
        """
        :param UserBean user_bean:
        :return int: the number of rows affected
        """
        query = UserModel.delete().where(UserModel.id == user_bean.primary_key)
        return query.execute()
