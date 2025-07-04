"""NOTE: Autogenerated. Do not edit the manually."""

from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server_template.models.base_model import Model
from server_template import util


class TemplatebackendExportTransformConfigReply(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, config=None):
        """TemplatebackendExportTransformConfigReply - a model defined in OpenAPI

        :param config: The config of this TemplatebackendExportTransformConfigReply.
        :type config: str
        """
        self.openapi_types = {
            'config': str
        }

        self.attribute_map = {
            'config': 'config'
        }

        self._config = config

    @classmethod
    def from_dict(cls, dikt) -> 'TemplatebackendExportTransformConfigReply':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The templatebackendExportTransformConfigReply of this TemplatebackendExportTransformConfigReply.
        :rtype: TemplatebackendExportTransformConfigReply
        """
        return util.deserialize_model(dikt, cls)

    @property
    def config(self) -> str:
        """Gets the config of this TemplatebackendExportTransformConfigReply.


        :return: The config of this TemplatebackendExportTransformConfigReply.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config: str):
        """Sets the config of this TemplatebackendExportTransformConfigReply.


        :param config: The config of this TemplatebackendExportTransformConfigReply.
        :type config: str
        """

        self._config = config
