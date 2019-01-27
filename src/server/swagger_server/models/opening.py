# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.move import Move  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class Opening(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, id: str=None, moves: List[Move]=None):  # noqa: E501
        """Opening - a model defined in Swagger

        :param name: The name of this Opening.  # noqa: E501
        :type name: str
        :param id: The id of this Opening.  # noqa: E501
        :type id: str
        :param moves: The moves of this Opening.  # noqa: E501
        :type moves: List[Move]
        """
        self.swagger_types = {
            'name': str,
            'id': str,
            'moves': List[Move]
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'moves': 'moves'
        }

        self._name = name
        self._id = id
        self._moves = moves

    @classmethod
    def from_dict(cls, dikt) -> 'Opening':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Opening of this Opening.  # noqa: E501
        :rtype: Opening
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Opening.


        :return: The name of this Opening.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Opening.


        :param name: The name of this Opening.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self) -> str:
        """Gets the id of this Opening.


        :return: The id of this Opening.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Opening.


        :param id: The id of this Opening.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and not re.search('[A-E][0-9]{2}', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/[A-E][0-9]{2}/`")  # noqa: E501

        self._id = id

    @property
    def moves(self) -> List[Move]:
        """Gets the moves of this Opening.


        :return: The moves of this Opening.
        :rtype: List[Move]
        """
        return self._moves

    @moves.setter
    def moves(self, moves: List[Move]):
        """Sets the moves of this Opening.


        :param moves: The moves of this Opening.
        :type moves: List[Move]
        """
        if moves is None:
            raise ValueError("Invalid value for `moves`, must not be `None`")  # noqa: E501

        self._moves = moves