"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template import util


class TemplatebackendShareReplyResult(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, success=None):
        """TemplatebackendShareReplyResult - a model defined in OpenAPI

        :param success: The success of this TemplatebackendShareReplyResult.
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
    def from_dict(cls, dikt) -> 'TemplatebackendShareReplyResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendShareReplyResult of this TemplatebackendShareReplyResult.
        :rtype: TemplatebackendShareReplyResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def success(self) -> bool:
        """Gets the success of this TemplatebackendShareReplyResult.


        :return: The success of this TemplatebackendShareReplyResult.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success: bool):
        """Sets the success of this TemplatebackendShareReplyResult.


        :param success: The success of this TemplatebackendShareReplyResult.
        :type success: bool
        """

        self._success = success
