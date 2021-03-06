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


class CheckpointingStatisticsCounts(object):
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
        'restored': 'int',
        'total': 'int',
        'in_progress': 'int',
        'completed': 'int',
        'failed': 'int'
    }

    attribute_map = {
        'restored': 'restored',
        'total': 'total',
        'in_progress': 'in_progress',
        'completed': 'completed',
        'failed': 'failed'
    }

    def __init__(self, restored=None, total=None, in_progress=None, completed=None, failed=None):  # noqa: E501
        """CheckpointingStatisticsCounts - a model defined in Swagger"""  # noqa: E501
        self._restored = None
        self._total = None
        self._in_progress = None
        self._completed = None
        self._failed = None
        self.discriminator = None
        if restored is not None:
            self.restored = restored
        if total is not None:
            self.total = total
        if in_progress is not None:
            self.in_progress = in_progress
        if completed is not None:
            self.completed = completed
        if failed is not None:
            self.failed = failed

    @property
    def restored(self):
        """Gets the restored of this CheckpointingStatisticsCounts.  # noqa: E501


        :return: The restored of this CheckpointingStatisticsCounts.  # noqa: E501
        :rtype: int
        """
        return self._restored

    @restored.setter
    def restored(self, restored):
        """Sets the restored of this CheckpointingStatisticsCounts.


        :param restored: The restored of this CheckpointingStatisticsCounts.  # noqa: E501
        :type: int
        """

        self._restored = restored

    @property
    def total(self):
        """Gets the total of this CheckpointingStatisticsCounts.  # noqa: E501


        :return: The total of this CheckpointingStatisticsCounts.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CheckpointingStatisticsCounts.


        :param total: The total of this CheckpointingStatisticsCounts.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def in_progress(self):
        """Gets the in_progress of this CheckpointingStatisticsCounts.  # noqa: E501


        :return: The in_progress of this CheckpointingStatisticsCounts.  # noqa: E501
        :rtype: int
        """
        return self._in_progress

    @in_progress.setter
    def in_progress(self, in_progress):
        """Sets the in_progress of this CheckpointingStatisticsCounts.


        :param in_progress: The in_progress of this CheckpointingStatisticsCounts.  # noqa: E501
        :type: int
        """

        self._in_progress = in_progress

    @property
    def completed(self):
        """Gets the completed of this CheckpointingStatisticsCounts.  # noqa: E501


        :return: The completed of this CheckpointingStatisticsCounts.  # noqa: E501
        :rtype: int
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this CheckpointingStatisticsCounts.


        :param completed: The completed of this CheckpointingStatisticsCounts.  # noqa: E501
        :type: int
        """

        self._completed = completed

    @property
    def failed(self):
        """Gets the failed of this CheckpointingStatisticsCounts.  # noqa: E501


        :return: The failed of this CheckpointingStatisticsCounts.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this CheckpointingStatisticsCounts.


        :param failed: The failed of this CheckpointingStatisticsCounts.  # noqa: E501
        :type: int
        """

        self._failed = failed

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
        if issubclass(CheckpointingStatisticsCounts, dict):
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
        if not isinstance(other, CheckpointingStatisticsCounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
