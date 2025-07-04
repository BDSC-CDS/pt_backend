"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template.models.templatebackend_list_transform_configs_result import TemplatebackendListTransformConfigsResult
from server_template import util

from server_template.models.templatebackend_list_transform_configs_result import TemplatebackendListTransformConfigsResult

class TemplatebackendListTransformConfigsReply(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result=None):
        """TemplatebackendListTransformConfigsReply - a model defined in OpenAPI

        :param result: The result of this TemplatebackendListTransformConfigsReply.
        :type result: TemplatebackendListTransformConfigsResult
        """
        self.openapi_types = {
            'result': TemplatebackendListTransformConfigsResult
        }

        self.attribute_map = {
            'result': 'result'
        }

        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendListTransformConfigsReply':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendListTransformConfigsReply of this TemplatebackendListTransformConfigsReply.
        :rtype: TemplatebackendListTransformConfigsReply
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> TemplatebackendListTransformConfigsResult:
        """Gets the result of this TemplatebackendListTransformConfigsReply.


        :return: The result of this TemplatebackendListTransformConfigsReply.
        :rtype: TemplatebackendListTransformConfigsResult
        """
        return self._result

    @result.setter
    def result(self, result: TemplatebackendListTransformConfigsResult):
        """Sets the result of this TemplatebackendListTransformConfigsReply.


        :param result: The result of this TemplatebackendListTransformConfigsReply.
        :type result: TemplatebackendListTransformConfigsResult
        """

        self._result = result
