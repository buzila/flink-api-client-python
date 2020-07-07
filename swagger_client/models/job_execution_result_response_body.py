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


class JobExecutionResultResponseBody(object):
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
        'status': 'QueueStatus',
        'job_execution_result': 'object'
    }

    attribute_map = {
        'status': 'status',
        'job_execution_result': 'job-execution-result'
    }

    def __init__(self, status=None, job_execution_result=None):  # noqa: E501
        """JobExecutionResultResponseBody - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._job_execution_result = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if job_execution_result is not None:
            self.job_execution_result = job_execution_result

    @property
    def status(self):
        """Gets the status of this JobExecutionResultResponseBody.  # noqa: E501


        :return: The status of this JobExecutionResultResponseBody.  # noqa: E501
        :rtype: QueueStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobExecutionResultResponseBody.


        :param status: The status of this JobExecutionResultResponseBody.  # noqa: E501
        :type: QueueStatus
        """

        self._status = status

    @property
    def job_execution_result(self):
        """Gets the job_execution_result of this JobExecutionResultResponseBody.  # noqa: E501


        :return: The job_execution_result of this JobExecutionResultResponseBody.  # noqa: E501
        :rtype: object
        """
        return self._job_execution_result

    @job_execution_result.setter
    def job_execution_result(self, job_execution_result):
        """Sets the job_execution_result of this JobExecutionResultResponseBody.


        :param job_execution_result: The job_execution_result of this JobExecutionResultResponseBody.  # noqa: E501
        :type: object
        """

        self._job_execution_result = job_execution_result

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
        if issubclass(JobExecutionResultResponseBody, dict):
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
        if not isinstance(other, JobExecutionResultResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
