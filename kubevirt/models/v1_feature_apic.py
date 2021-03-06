# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1FeatureAPIC(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'end_of_interrupt': 'bool'
    }

    attribute_map = {
        'enabled': 'enabled',
        'end_of_interrupt': 'endOfInterrupt'
    }

    def __init__(self, enabled=None, end_of_interrupt=None):
        """
        V1FeatureAPIC - a model defined in Swagger
        """

        self._enabled = None
        self._end_of_interrupt = None

        if enabled is not None:
          self.enabled = enabled
        if end_of_interrupt is not None:
          self.end_of_interrupt = end_of_interrupt

    @property
    def enabled(self):
        """
        Gets the enabled of this V1FeatureAPIC.
        Enabled determines if the feature should be enabled or disabled on the guest. Defaults to true.

        :return: The enabled of this V1FeatureAPIC.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this V1FeatureAPIC.
        Enabled determines if the feature should be enabled or disabled on the guest. Defaults to true.

        :param enabled: The enabled of this V1FeatureAPIC.
        :type: bool
        """

        self._enabled = enabled

    @property
    def end_of_interrupt(self):
        """
        Gets the end_of_interrupt of this V1FeatureAPIC.
        EndOfInterrupt enables the end of interrupt notification in the guest. Defaults to false.

        :return: The end_of_interrupt of this V1FeatureAPIC.
        :rtype: bool
        """
        return self._end_of_interrupt

    @end_of_interrupt.setter
    def end_of_interrupt(self, end_of_interrupt):
        """
        Sets the end_of_interrupt of this V1FeatureAPIC.
        EndOfInterrupt enables the end of interrupt notification in the guest. Defaults to false.

        :param end_of_interrupt: The end_of_interrupt of this V1FeatureAPIC.
        :type: bool
        """

        self._end_of_interrupt = end_of_interrupt

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
        if not isinstance(other, V1FeatureAPIC):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
