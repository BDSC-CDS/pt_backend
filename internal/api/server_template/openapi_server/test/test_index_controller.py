import unittest

from flask import json

from openapi_server.models.index_service_create_hello_request import IndexServiceCreateHelloRequest  # noqa: E501
from openapi_server.models.rpc_status import RpcStatus  # noqa: E501
from openapi_server.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply  # noqa: E501
from openapi_server.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply  # noqa: E501
from openapi_server.test import BaseTestCase


class TestIndexController(BaseTestCase):
    """IndexController integration test stubs"""

    def test_index_service_create_hello(self):
        """Test case for index_service_create_hello

        Get a hello
        """
        body = openapi_server.IndexServiceCreateHelloRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Bearer': 'special-key',
        }
        response = self.client.open(
            '/api/v1/hello/{identifier}'.format(identifier=56),
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_service_get_hello(self):
        """Test case for index_service_get_hello

        Get a hello
        """
        headers = { 
            'Accept': 'application/json',
            'Bearer': 'special-key',
        }
        response = self.client.open(
            '/api/v1/hello',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_index_service_get_helloo(self):
        """Test case for index_service_get_helloo

        Get a hello
        """
        headers = { 
            'Accept': 'application/json',
            'Bearer': 'special-key',
        }
        response = self.client.open(
            '/api/v1/helloo',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
