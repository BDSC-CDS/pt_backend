# coding: utf-8

"""
    Api Documentation

    Api Documentation

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from openapi_client.models.result_metadata import ResultMetadata

class TestResultMetadata(unittest.TestCase):
    """ResultMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResultMetadata:
        """Test ResultMetadata
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResultMetadata`
        """
        model = ResultMetadata()
        if include_optional:
            return ResultMetadata(
                id = 56
            )
        else:
            return ResultMetadata(
        )
        """

    def testResultMetadata(self):
        """Test ResultMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
