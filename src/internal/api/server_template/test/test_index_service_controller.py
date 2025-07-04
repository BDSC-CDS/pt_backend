"""NOTE: Autogenerated. Do not edit the manually."""

import unittest

from flask import json

from server_template.models.index_service_create_hello_request import IndexServiceCreateHelloRequest
from server_template.models.rpc_status import RpcStatus
from server_template.models.templatebackend_create_hello_reply import TemplatebackendCreateHelloReply
from server_template.models.templatebackend_get_hello_reply import TemplatebackendGetHelloReply
from server_template.test import BaseTestCase


class TestIndexServiceController(BaseTestCase):
    """IndexServiceController integration test stubs"""

    def test_index_service_create_hello(self):
        """Test case for index_service_create_hello

        Get a hello
        """
        body = server_template.IndexServiceCreateHelloRequest()
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


if __name__ == '__main__':
    unittest.main()
