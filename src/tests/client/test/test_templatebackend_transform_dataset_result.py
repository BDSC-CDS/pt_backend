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

from openapi_client.models.templatebackend_transform_dataset_result import TemplatebackendTransformDatasetResult

class TestTemplatebackendTransformDatasetResult(unittest.TestCase):
    """TemplatebackendTransformDatasetResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplatebackendTransformDatasetResult:
        """Test TemplatebackendTransformDatasetResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplatebackendTransformDatasetResult`
        """
        model = TemplatebackendTransformDatasetResult()
        if include_optional:
            return TemplatebackendTransformDatasetResult(
                id = 56
            )
        else:
            return TemplatebackendTransformDatasetResult(
        )
        """

    def testTemplatebackendTransformDatasetResult(self):
        """Test TemplatebackendTransformDatasetResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
