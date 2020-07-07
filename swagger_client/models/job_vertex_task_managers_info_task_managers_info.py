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


class JobVertexTaskManagersInfoTaskManagersInfo(object):
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
        'host': 'str',
        'status': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'duration': 'int',
        'metrics': 'IOMetricsInfo',
        'status_counts': 'dict(str, int)'
    }

    attribute_map = {
        'host': 'host',
        'status': 'status',
        'start_time': 'start-time',
        'end_time': 'end-time',
        'duration': 'duration',
        'metrics': 'metrics',
        'status_counts': 'status-counts'
    }

    def __init__(self, host=None, status=None, start_time=None, end_time=None, duration=None, metrics=None, status_counts=None):  # noqa: E501
        """JobVertexTaskManagersInfoTaskManagersInfo - a model defined in Swagger"""  # noqa: E501
        self._host = None
        self._status = None
        self._start_time = None
        self._end_time = None
        self._duration = None
        self._metrics = None
        self._status_counts = None
        self.discriminator = None
        if host is not None:
            self.host = host
        if status is not None:
            self.status = status
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if metrics is not None:
            self.metrics = metrics
        if status_counts is not None:
            self.status_counts = status_counts

    @property
    def host(self):
        """Gets the host of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The host of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param host: The host of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def status(self):
        """Gets the status of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The status of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param status: The status of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "SCHEDULED", "DEPLOYING", "RUNNING", "FINISHED", "CANCELING", "CANCELED", "FAILED", "RECONCILING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def start_time(self):
        """Gets the start_time of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The start_time of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param start_time: The start_time of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: int
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The end_time of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param end_time: The end_time of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: int
        """

        self._end_time = end_time

    @property
    def duration(self):
        """Gets the duration of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The duration of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param duration: The duration of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def metrics(self):
        """Gets the metrics of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The metrics of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: IOMetricsInfo
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param metrics: The metrics of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: IOMetricsInfo
        """

        self._metrics = metrics

    @property
    def status_counts(self):
        """Gets the status_counts of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501


        :return: The status_counts of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._status_counts

    @status_counts.setter
    def status_counts(self, status_counts):
        """Sets the status_counts of this JobVertexTaskManagersInfoTaskManagersInfo.


        :param status_counts: The status_counts of this JobVertexTaskManagersInfoTaskManagersInfo.  # noqa: E501
        :type: dict(str, int)
        """

        self._status_counts = status_counts

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
        if issubclass(JobVertexTaskManagersInfoTaskManagersInfo, dict):
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
        if not isinstance(other, JobVertexTaskManagersInfoTaskManagersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other