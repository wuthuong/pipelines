# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class V2beta1Pipeline(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pipeline_id': 'str',
        'display_name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'namespace': 'str',
        'error': 'RpcStatus'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'display_name': 'display_name',
        'description': 'description',
        'created_at': 'created_at',
        'namespace': 'namespace',
        'error': 'error'
    }

    def __init__(self, pipeline_id=None, display_name=None, description=None, created_at=None, namespace=None, error=None, local_vars_configuration=None):  # noqa: E501
        """V2beta1Pipeline - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pipeline_id = None
        self._display_name = None
        self._description = None
        self._created_at = None
        self._namespace = None
        self._error = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if namespace is not None:
            self.namespace = namespace
        if error is not None:
            self.error = error

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this V2beta1Pipeline.  # noqa: E501

        Output. Unique pipeline ID. Generated by API server.  # noqa: E501

        :return: The pipeline_id of this V2beta1Pipeline.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this V2beta1Pipeline.

        Output. Unique pipeline ID. Generated by API server.  # noqa: E501

        :param pipeline_id: The pipeline_id of this V2beta1Pipeline.  # noqa: E501
        :type pipeline_id: str
        """

        self._pipeline_id = pipeline_id

    @property
    def display_name(self):
        """Gets the display_name of this V2beta1Pipeline.  # noqa: E501

        Required input field. Pipeline name provided by user. If not specified, file name is used as pipeline name.  # noqa: E501

        :return: The display_name of this V2beta1Pipeline.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this V2beta1Pipeline.

        Required input field. Pipeline name provided by user. If not specified, file name is used as pipeline name.  # noqa: E501

        :param display_name: The display_name of this V2beta1Pipeline.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this V2beta1Pipeline.  # noqa: E501

        Optional input field. A short description of the pipeline.  # noqa: E501

        :return: The description of this V2beta1Pipeline.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V2beta1Pipeline.

        Optional input field. A short description of the pipeline.  # noqa: E501

        :param description: The description of this V2beta1Pipeline.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this V2beta1Pipeline.  # noqa: E501

        Output. Creation time of the pipeline.  # noqa: E501

        :return: The created_at of this V2beta1Pipeline.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this V2beta1Pipeline.

        Output. Creation time of the pipeline.  # noqa: E501

        :param created_at: The created_at of this V2beta1Pipeline.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def namespace(self):
        """Gets the namespace of this V2beta1Pipeline.  # noqa: E501

        Input. A namespace this pipeline belongs to. Causes error if user is not authorized to access the specified namespace. If not specified in CreatePipeline, default namespace is used.  # noqa: E501

        :return: The namespace of this V2beta1Pipeline.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this V2beta1Pipeline.

        Input. A namespace this pipeline belongs to. Causes error if user is not authorized to access the specified namespace. If not specified in CreatePipeline, default namespace is used.  # noqa: E501

        :param namespace: The namespace of this V2beta1Pipeline.  # noqa: E501
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def error(self):
        """Gets the error of this V2beta1Pipeline.  # noqa: E501


        :return: The error of this V2beta1Pipeline.  # noqa: E501
        :rtype: RpcStatus
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this V2beta1Pipeline.


        :param error: The error of this V2beta1Pipeline.  # noqa: E501
        :type error: RpcStatus
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V2beta1Pipeline):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V2beta1Pipeline):
            return True

        return self.to_dict() != other.to_dict()
