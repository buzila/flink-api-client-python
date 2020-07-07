# coding: utf-8

"""
    Flink API Client

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class HardwareDescription(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'cpu_cores': 'int',
        'physical_memory': 'int',
        'free_memory': 'int',
        'managed_memory': 'int'
    }

    attribute_map = {
        'cpu_cores': 'cpuCores',
        'physical_memory': 'physicalMemory',
        'free_memory': 'freeMemory',
        'managed_memory': 'managedMemory'
    }

    def __init__(self, cpu_cores=None, physical_memory=None, free_memory=None, managed_memory=None):  # noqa: E501
        """HardwareDescription - a model defined in Swagger"""  # noqa: E501
        self._cpu_cores = None
        self._physical_memory = None
        self._free_memory = None
        self._managed_memory = None
        self.discriminator = None
        if cpu_cores is not None:
            self.cpu_cores = cpu_cores
        if physical_memory is not None:
            self.physical_memory = physical_memory
        if free_memory is not None:
            self.free_memory = free_memory
        if managed_memory is not None:
            self.managed_memory = managed_memory

    @property
    def cpu_cores(self):
        """Gets the cpu_cores of this HardwareDescription.  # noqa: E501


        :return: The cpu_cores of this HardwareDescription.  # noqa: E501
        :rtype: int
        """
        return self._cpu_cores

    @cpu_cores.setter
    def cpu_cores(self, cpu_cores):
        """Sets the cpu_cores of this HardwareDescription.


        :param cpu_cores: The cpu_cores of this HardwareDescription.  # noqa: E501
        :type: int
        """

        self._cpu_cores = cpu_cores

    @property
    def physical_memory(self):
        """Gets the physical_memory of this HardwareDescription.  # noqa: E501


        :return: The physical_memory of this HardwareDescription.  # noqa: E501
        :rtype: int
        """
        return self._physical_memory

    @physical_memory.setter
    def physical_memory(self, physical_memory):
        """Sets the physical_memory of this HardwareDescription.


        :param physical_memory: The physical_memory of this HardwareDescription.  # noqa: E501
        :type: int
        """

        self._physical_memory = physical_memory

    @property
    def free_memory(self):
        """Gets the free_memory of this HardwareDescription.  # noqa: E501


        :return: The free_memory of this HardwareDescription.  # noqa: E501
        :rtype: int
        """
        return self._free_memory

    @free_memory.setter
    def free_memory(self, free_memory):
        """Sets the free_memory of this HardwareDescription.


        :param free_memory: The free_memory of this HardwareDescription.  # noqa: E501
        :type: int
        """

        self._free_memory = free_memory

    @property
    def managed_memory(self):
        """Gets the managed_memory of this HardwareDescription.  # noqa: E501


        :return: The managed_memory of this HardwareDescription.  # noqa: E501
        :rtype: int
        """
        return self._managed_memory

    @managed_memory.setter
    def managed_memory(self, managed_memory):
        """Sets the managed_memory of this HardwareDescription.


        :param managed_memory: The managed_memory of this HardwareDescription.  # noqa: E501
        :type: int
        """

        self._managed_memory = managed_memory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(HardwareDescription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HardwareDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
