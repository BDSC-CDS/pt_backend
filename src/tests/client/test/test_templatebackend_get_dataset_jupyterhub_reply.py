# coding: utf-8

"""
    pt backend

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Contact: development.bdsc@chuv.ch
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.templatebackend_get_dataset_jupyterhub_reply import TemplatebackendGetDatasetJupyterhubReply

class TestTemplatebackendGetDatasetJupyterhubReply(unittest.TestCase):
    """TemplatebackendGetDatasetJupyterhubReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplatebackendGetDatasetJupyterhubReply:
        """Test TemplatebackendGetDatasetJupyterhubReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplatebackendGetDatasetJupyterhubReply`
        """
        model = TemplatebackendGetDatasetJupyterhubReply()
        if include_optional:
            return TemplatebackendGetDatasetJupyterhubReply(
                result = openapi_client.models.templatebackend_get_dataset_jupyterhub_result.templatebackendGetDatasetJupyterhubResult(
                    url = '', )
            )
        else:
            return TemplatebackendGetDatasetJupyterhubReply(
        )
        """

    def testTemplatebackendGetDatasetJupyterhubReply(self):
        """Test TemplatebackendGetDatasetJupyterhubReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
