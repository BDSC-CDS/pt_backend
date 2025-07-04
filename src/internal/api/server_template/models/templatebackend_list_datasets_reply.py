"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template.models.templatebackend_list_datasets_result import TemplatebackendListDatasetsResult
from server_template import util

from server_template.models.templatebackend_list_datasets_result import TemplatebackendListDatasetsResult

class TemplatebackendListDatasetsReply(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result=None):
        """TemplatebackendListDatasetsReply - a model defined in OpenAPI

        :param result: The result of this TemplatebackendListDatasetsReply.
        :type result: TemplatebackendListDatasetsResult
        """
        self.openapi_types = {
            'result': TemplatebackendListDatasetsResult
        }

        self.attribute_map = {
            'result': 'result'
        }

        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendListDatasetsReply':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendListDatasetsReply of this TemplatebackendListDatasetsReply.
        :rtype: TemplatebackendListDatasetsReply
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> TemplatebackendListDatasetsResult:
        """Gets the result of this TemplatebackendListDatasetsReply.


        :return: The result of this TemplatebackendListDatasetsReply.
        :rtype: TemplatebackendListDatasetsResult
        """
        return self._result

    @result.setter
    def result(self, result: TemplatebackendListDatasetsResult):
        """Sets the result of this TemplatebackendListDatasetsReply.


        :param result: The result of this TemplatebackendListDatasetsReply.
        :type result: TemplatebackendListDatasetsResult
        """

        self._result = result
