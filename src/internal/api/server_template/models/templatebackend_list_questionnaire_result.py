"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template.models.templatebackend_questionnaire import TemplatebackendQuestionnaire
from server_template import util

from server_template.models.templatebackend_questionnaire import TemplatebackendQuestionnaire

class TemplatebackendListQuestionnaireResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, questionnaires=None):
        """TemplatebackendListQuestionnaireResult - a model defined in OpenAPI

        :param questionnaires: The questionnaires of this TemplatebackendListQuestionnaireResult.
        :type questionnaires: List[TemplatebackendQuestionnaire]
        """
        self.openapi_types = {
            'questionnaires': List[TemplatebackendQuestionnaire]
        }

        self.attribute_map = {
            'questionnaires': 'questionnaires'
        }

        self._questionnaires = questionnaires

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendListQuestionnaireResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendListQuestionnaireResult of this TemplatebackendListQuestionnaireResult.
        :rtype: TemplatebackendListQuestionnaireResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def questionnaires(self) -> List[TemplatebackendQuestionnaire]:
        """Gets the questionnaires of this TemplatebackendListQuestionnaireResult.


        :return: The questionnaires of this TemplatebackendListQuestionnaireResult.
        :rtype: List[TemplatebackendQuestionnaire]
        """
        return self._questionnaires

    @questionnaires.setter
    def questionnaires(self, questionnaires: List[TemplatebackendQuestionnaire]):
        """Sets the questionnaires of this TemplatebackendListQuestionnaireResult.


        :param questionnaires: The questionnaires of this TemplatebackendListQuestionnaireResult.
        :type questionnaires: List[TemplatebackendQuestionnaire]
        """

        self._questionnaires = questionnaires
