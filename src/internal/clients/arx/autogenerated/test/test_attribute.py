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

from openapi_client.models.attribute import Attribute

class TestAttribute(unittest.TestCase):
    """Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attribute:
        """Test Attribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attribute`
        """
        model = Attribute()
        if include_optional:
            return Attribute(
                arx_name = '',
                attribute_type = 'QUASI_IDENTIFYING_ATTRIBUTE',
                dataset_name = '',
                var_date = True,
                hierarchy = [
                    [
                        ''
                        ]
                    ],
                identifying = True,
                ippor_numero_sejour = True,
                quasi_identifying = True,
                sensitive = True,
                weight = 1.337
            )
        else:
            return Attribute(
        )
        """

    def testAttribute(self):
        """Test Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
