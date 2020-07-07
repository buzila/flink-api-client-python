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


class SubtaskExecutionAttemptAccumulatorsInfo(object):
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
        'attempt': 'int',
        'id': 'str',
        'user_accumulators': 'list[UserAccumulator]'
    }

    attribute_map = {
        'subtask': 'subtask',
        'attempt': 'attempt',
        'id': 'id',
        'user_accumulators': 'user-accumulators'
    }

    def __init__(self, subtask=None, attempt=None, id=None, user_accumulators=None):  # noqa: E501
        """SubtaskExecutionAttemptAccumulatorsInfo - a model defined in Swagger"""  # noqa: E501
        self._subtask = None
        self._attempt = None
        self._id = None
        self._user_accumulators = None
        self.discriminator = None
        if subtask is not None:
            self.subtask = subtask
        if attempt is not None:
            self.attempt = attempt
        if id is not None:
            self.id = id
        if user_accumulators is not None:
            self.user_accumulators = user_accumulators

    @property
    def subtask(self):
        """Gets the subtask of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501


        :return: The subtask of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :rtype: int
        """
        return self._subtask

    @subtask.setter
    def subtask(self, subtask):
        """Sets the subtask of this SubtaskExecutionAttemptAccumulatorsInfo.


        :param subtask: The subtask of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :type: int
        """

        self._subtask = subtask

    @property
    def attempt(self):
        """Gets the attempt of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501


        :return: The attempt of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :rtype: int
        """
        return self._attempt

    @attempt.setter
    def attempt(self, attempt):
        """Sets the attempt of this SubtaskExecutionAttemptAccumulatorsInfo.


        :param attempt: The attempt of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :type: int
        """

        self._attempt = attempt

    @property
    def id(self):
        """Gets the id of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501


        :return: The id of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubtaskExecutionAttemptAccumulatorsInfo.


        :param id: The id of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_accumulators(self):
        """Gets the user_accumulators of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501


        :return: The user_accumulators of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :rtype: list[UserAccumulator]
        """
        return self._user_accumulators

    @user_accumulators.setter
    def user_accumulators(self, user_accumulators):
        """Sets the user_accumulators of this SubtaskExecutionAttemptAccumulatorsInfo.


        :param user_accumulators: The user_accumulators of this SubtaskExecutionAttemptAccumulatorsInfo.  # noqa: E501
        :type: list[UserAccumulator]
        """

        self._user_accumulators = user_accumulators

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
        if issubclass(SubtaskExecutionAttemptAccumulatorsInfo, dict):
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
        if not isinstance(other, SubtaskExecutionAttemptAccumulatorsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
