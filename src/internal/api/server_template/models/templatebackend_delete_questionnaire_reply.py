"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template.models.templatebackend_delete_questionnaire_result import TemplatebackendDeleteQuestionnaireResult
from server_template import util

from server_template.models.templatebackend_delete_questionnaire_result import TemplatebackendDeleteQuestionnaireResult

class TemplatebackendDeleteQuestionnaireReply(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result=None):
        """TemplatebackendDeleteQuestionnaireReply - a model defined in OpenAPI

        :param result: The result of this TemplatebackendDeleteQuestionnaireReply.
        :type result: TemplatebackendDeleteQuestionnaireResult
        """
        self.openapi_types = {
            'result': TemplatebackendDeleteQuestionnaireResult
        }

        self.attribute_map = {
            'result': 'result'
        }

        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendDeleteQuestionnaireReply':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendDeleteQuestionnaireReply of this TemplatebackendDeleteQuestionnaireReply.
        :rtype: TemplatebackendDeleteQuestionnaireReply
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> TemplatebackendDeleteQuestionnaireResult:
        """Gets the result of this TemplatebackendDeleteQuestionnaireReply.


        :return: The result of this TemplatebackendDeleteQuestionnaireReply.
        :rtype: TemplatebackendDeleteQuestionnaireResult
        """
        return self._result

    @result.setter
    def result(self, result: TemplatebackendDeleteQuestionnaireResult):
        """Sets the result of this TemplatebackendDeleteQuestionnaireReply.


        :param result: The result of this TemplatebackendDeleteQuestionnaireReply.
        :type result: TemplatebackendDeleteQuestionnaireResult
        """

        self._result = result
