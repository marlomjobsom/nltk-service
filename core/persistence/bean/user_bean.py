#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
User Bean
"""


class UserBean:
    """
    User Bean
    """

    def __init__(self, user_model_instance):
        """
        :param core.persistence.model.user_model.UserModel user_model_instance:
        """
        self._primary_key = user_model_instance.id
        self._name = user_model_instance.name
        self._token = user_model_instance.token

    def __eq__(self, other):
        result = False

        if isinstance(other, self.__class__):
            result = self.__dict__ == other.__dict__

        return result

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def primary_key(self):
        """
        :return int:
        """
        return self._primary_key

    @property
    def name(self):
        """
        :return str:
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        :param str name:
        """
        self._name = name

    @property
    def token(self):
        """
        :return str:
        """
        return self._token

    def to_dict(self):
        """
        :return dict:
        """
        return dict(name=self.name, token=self.token)
