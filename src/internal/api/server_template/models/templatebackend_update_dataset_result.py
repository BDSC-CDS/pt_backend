"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template import util


class TemplatebackendUpdateDatasetResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, success=None):
        """TemplatebackendUpdateDatasetResult - a model defined in OpenAPI

        :param success: The success of this TemplatebackendUpdateDatasetResult.
        :type success: bool
        """
        self.openapi_types = {
            'success': bool
        }

        self.attribute_map = {
            'success': 'success'
        }

        self._success = success

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendUpdateDatasetResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendUpdateDatasetResult of this TemplatebackendUpdateDatasetResult.
        :rtype: TemplatebackendUpdateDatasetResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def success(self) -> bool:
        """Gets the success of this TemplatebackendUpdateDatasetResult.


        :return: The success of this TemplatebackendUpdateDatasetResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this TemplatebackendUpdateDatasetResult.


        :param success: The success of this TemplatebackendUpdateDatasetResult.
        :type success: bool
        """

        self._success = success
