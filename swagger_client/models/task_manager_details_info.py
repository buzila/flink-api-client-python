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


class TaskManagerDetailsInfo(object):
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
        'id': 'str',
        'path': 'str',
        'data_port': 'int',
        'time_since_last_heartbeat': 'int',
        'slots_number': 'int',
        'free_slots': 'int',
        'hardware': 'HardwareDescription',
        'metrics': 'TaskManagerMetricsInfo'
    }

    attribute_map = {
        'id': 'id',
        'path': 'path',
        'data_port': 'dataPort',
        'time_since_last_heartbeat': 'timeSinceLastHeartbeat',
        'slots_number': 'slotsNumber',
        'free_slots': 'freeSlots',
        'hardware': 'hardware',
        'metrics': 'metrics'
    }

    def __init__(self, id=None, path=None, data_port=None, time_since_last_heartbeat=None, slots_number=None, free_slots=None, hardware=None, metrics=None):  # noqa: E501
        """TaskManagerDetailsInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._path = None
        self._data_port = None
        self._time_since_last_heartbeat = None
        self._slots_number = None
        self._free_slots = None
        self._hardware = None
        self._metrics = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if path is not None:
            self.path = path
        if data_port is not None:
            self.data_port = data_port
        if time_since_last_heartbeat is not None:
            self.time_since_last_heartbeat = time_since_last_heartbeat
        if slots_number is not None:
            self.slots_number = slots_number
        if free_slots is not None:
            self.free_slots = free_slots
        if hardware is not None:
            self.hardware = hardware
        if metrics is not None:
            self.metrics = metrics

    @property
    def id(self):
        """Gets the id of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The id of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskManagerDetailsInfo.


        :param id: The id of this TaskManagerDetailsInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def path(self):
        """Gets the path of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The path of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TaskManagerDetailsInfo.


        :param path: The path of this TaskManagerDetailsInfo.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def data_port(self):
        """Gets the data_port of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The data_port of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._data_port

    @data_port.setter
    def data_port(self, data_port):
        """Sets the data_port of this TaskManagerDetailsInfo.


        :param data_port: The data_port of this TaskManagerDetailsInfo.  # noqa: E501
        :type: int
        """

        self._data_port = data_port

    @property
    def time_since_last_heartbeat(self):
        """Gets the time_since_last_heartbeat of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The time_since_last_heartbeat of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._time_since_last_heartbeat

    @time_since_last_heartbeat.setter
    def time_since_last_heartbeat(self, time_since_last_heartbeat):
        """Sets the time_since_last_heartbeat of this TaskManagerDetailsInfo.


        :param time_since_last_heartbeat: The time_since_last_heartbeat of this TaskManagerDetailsInfo.  # noqa: E501
        :type: int
        """

        self._time_since_last_heartbeat = time_since_last_heartbeat

    @property
    def slots_number(self):
        """Gets the slots_number of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The slots_number of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._slots_number

    @slots_number.setter
    def slots_number(self, slots_number):
        """Sets the slots_number of this TaskManagerDetailsInfo.


        :param slots_number: The slots_number of this TaskManagerDetailsInfo.  # noqa: E501
        :type: int
        """

        self._slots_number = slots_number

    @property
    def free_slots(self):
        """Gets the free_slots of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The free_slots of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: int
        """
        return self._free_slots

    @free_slots.setter
    def free_slots(self, free_slots):
        """Sets the free_slots of this TaskManagerDetailsInfo.


        :param free_slots: The free_slots of this TaskManagerDetailsInfo.  # noqa: E501
        :type: int
        """

        self._free_slots = free_slots

    @property
    def hardware(self):
        """Gets the hardware of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The hardware of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: HardwareDescription
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this TaskManagerDetailsInfo.


        :param hardware: The hardware of this TaskManagerDetailsInfo.  # noqa: E501
        :type: HardwareDescription
        """

        self._hardware = hardware

    @property
    def metrics(self):
        """Gets the metrics of this TaskManagerDetailsInfo.  # noqa: E501


        :return: The metrics of this TaskManagerDetailsInfo.  # noqa: E501
        :rtype: TaskManagerMetricsInfo
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this TaskManagerDetailsInfo.


        :param metrics: The metrics of this TaskManagerDetailsInfo.  # noqa: E501
        :type: TaskManagerMetricsInfo
        """

        self._metrics = metrics

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
        if issubclass(TaskManagerDetailsInfo, dict):
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
        if not isinstance(other, TaskManagerDetailsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
