# coding: utf-8

"""
    Api Documentation

    Api Documentation

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.records_api_api import RecordsApiApi


class TestRecordsApiApi(unittest.TestCase):
    """RecordsApiApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecordsApiApi()

    def tearDown(self) -> None:
        pass

    def test_get_all_records_using_get(self) -> None:
        """Test case for get_all_records_using_get

        getAllRecords
        """
        pass

    def test_get_records_by_period_and_username_using_get(self) -> None:
        """Test case for get_records_by_period_and_username_using_get

        getRecordsByPeriodAndUsername
        """
        pass

    def test_get_records_by_period_using_get(self) -> None:
        """Test case for get_records_by_period_using_get

        getRecordsByPeriod
        """
        pass

    def test_get_records_by_username_using_get(self) -> None:
        """Test case for get_records_by_username_using_get

        getRecordsByUsername
        """
        pass


if __name__ == '__main__':
    unittest.main()
