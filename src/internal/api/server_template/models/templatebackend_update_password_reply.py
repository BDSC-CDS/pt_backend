"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template import util


class TemplatebackendUpdatePasswordReply(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result=None):
        """TemplatebackendUpdatePasswordReply - a model defined in OpenAPI

        :param result: The result of this TemplatebackendUpdatePasswordReply.
        :type result: object
        """
        self.openapi_types = {
            'result': object
        }

        self.attribute_map = {
            'result': 'result'
        }

        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendUpdatePasswordReply':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendUpdatePasswordReply of this TemplatebackendUpdatePasswordReply.
        :rtype: TemplatebackendUpdatePasswordReply
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self) -> object:
        """Gets the result of this TemplatebackendUpdatePasswordReply.


        :return: The result of this TemplatebackendUpdatePasswordReply.
        :rtype: object
        """
        return self._result

    @result.setter
    def result(self, result: object):
        """Sets the result of this TemplatebackendUpdatePasswordReply.


        :param result: The result of this TemplatebackendUpdatePasswordReply.
        :type result: object
        """

        self._result = result
