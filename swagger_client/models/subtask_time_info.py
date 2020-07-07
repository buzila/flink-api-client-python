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


class SubtaskTimeInfo(object):
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
        'subtask': 'int',
        'host': 'str',
        'duration': 'int',
        'timestamps': 'dict(str, int)'
    }

    attribute_map = {
        'subtask': 'subtask',
        'host': 'host',
        'duration': 'duration',
        'timestamps': 'timestamps'
    }

    def __init__(self, subtask=None, host=None, duration=None, timestamps=None):  # noqa: E501
        """SubtaskTimeInfo - a model defined in Swagger"""  # noqa: E501
        self._subtask = None
        self._host = None
        self._duration = None
        self._timestamps = None
        self.discriminator = None
        if subtask is not None:
            self.subtask = subtask
        if host is not None:
            self.host = host
        if duration is not None:
            self.duration = duration
        if timestamps is not None:
            self.timestamps = timestamps

    @property
    def subtask(self):
        """Gets the subtask of this SubtaskTimeInfo.  # noqa: E501


        :return: The subtask of this SubtaskTimeInfo.  # noqa: E501
        :rtype: int
        """
        return self._subtask

    @subtask.setter
    def subtask(self, subtask):
        """Sets the subtask of this SubtaskTimeInfo.


        :param subtask: The subtask of this SubtaskTimeInfo.  # noqa: E501
        :type: int
        """

        self._subtask = subtask

    @property
    def host(self):
        """Gets the host of this SubtaskTimeInfo.  # noqa: E501


        :return: The host of this SubtaskTimeInfo.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SubtaskTimeInfo.


        :param host: The host of this SubtaskTimeInfo.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def duration(self):
        """Gets the duration of this SubtaskTimeInfo.  # noqa: E501


        :return: The duration of this SubtaskTimeInfo.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SubtaskTimeInfo.


        :param duration: The duration of this SubtaskTimeInfo.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def timestamps(self):
        """Gets the timestamps of this SubtaskTimeInfo.  # noqa: E501


        :return: The timestamps of this SubtaskTimeInfo.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this SubtaskTimeInfo.


        :param timestamps: The timestamps of this SubtaskTimeInfo.  # noqa: E501
        :type: dict(str, int)
        """

        self._timestamps = timestamps

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
        if issubclass(SubtaskTimeInfo, dict):
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
        if not isinstance(other, SubtaskTimeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other