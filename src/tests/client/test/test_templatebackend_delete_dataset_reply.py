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

from openapi_client.models.templatebackend_delete_dataset_reply import TemplatebackendDeleteDatasetReply

class TestTemplatebackendDeleteDatasetReply(unittest.TestCase):
    """TemplatebackendDeleteDatasetReply unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplatebackendDeleteDatasetReply:
        """Test TemplatebackendDeleteDatasetReply
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplatebackendDeleteDatasetReply`
        """
        model = TemplatebackendDeleteDatasetReply()
        if include_optional:
            return TemplatebackendDeleteDatasetReply(
                result = openapi_client.models.templatebackend_delete_dataset_result.templatebackendDeleteDatasetResult(
                    success = True, )
            )
        else:
            return TemplatebackendDeleteDatasetReply(
        )
        """

    def testTemplatebackendDeleteDatasetReply(self):
        """Test TemplatebackendDeleteDatasetReply"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
