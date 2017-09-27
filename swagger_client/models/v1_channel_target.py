# coding: utf-8

"""


    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version:

    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1ChannelTarget(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, type=None, address=None, port=None):
        """
        V1ChannelTarget - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'address': 'str',
            'port': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'address': 'address',
            'port': 'port'
        }

        self._name = name
        self._type = type
        self._address = address
        self._port = port

    @property
    def name(self):
        """
        Gets the name of this V1ChannelTarget.


        :return: The name of this V1ChannelTarget.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1ChannelTarget.


        :param name: The name of this V1ChannelTarget.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this V1ChannelTarget.


        :return: The type of this V1ChannelTarget.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ChannelTarget.


        :param type: The type of this V1ChannelTarget.
        :type: str
        """

        self._type = type

    @property
    def address(self):
        """
        Gets the address of this V1ChannelTarget.


        :return: The address of this V1ChannelTarget.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this V1ChannelTarget.


        :param address: The address of this V1ChannelTarget.
        :type: str
        """

        self._address = address

    @property
    def port(self):
        """
        Gets the port of this V1ChannelTarget.


        :return: The port of this V1ChannelTarget.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this V1ChannelTarget.


        :param port: The port of this V1ChannelTarget.
        :type: int
        """

        self._port = port

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
