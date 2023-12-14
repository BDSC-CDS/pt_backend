import unittest
import openapi_client
from pprint import pprint
from src.tests.acceptance.helpers.client import client

class TestUser(unittest.TestCase):
    def test_create_user(self):
        with client() as api_client:
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