import unittest
import time
import os
import sys
import traceback

### Allow dynamic import resolution from generated template backend
# Get the absolute path to src/internal/api/
module_path = os.path.abspath(os.path.join('src', 'tests', 'client'))
# Add this path to sys.path if it's not already there
if module_path not in sys.path:
    sys.path.append(module_path)

import openapi_client
from openapi_client.models.templatebackend_create_user_reply import TemplatebackendCreateUserReply
from openapi_client.models.templatebackend_user import TemplatebackendUser
from openapi_client.rest import ApiException
from pprint import pprint


class TestUser(unittest.TestCase):

    def test_create_user(self):
        configuration = openapi_client.Configuration(
            host = "http://127.0.0.1:5000"
        )
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.UsersApi(api_client)
            body = openapi_client.TemplatebackendUser(
                password="hello", 
                username="moto2", 
                email="hello.moto@gmail.com",
                firstName="hello",
                lastName="moto"
            )
            api_response = api_instance.user_service_create_user(body)
            print("The response of UsersApi->user_service_create_user:\n")
            pprint(api_response)

        self.assertIsNotNone(api_response)
        self.assertIsInstance(api_response.result.id, str)
        id = int(api_response.result.id)
        self.assertIsInstance(id, int)
        self.assertTrue(id > 0)

if __name__ == '__main__':
    unittest.main()