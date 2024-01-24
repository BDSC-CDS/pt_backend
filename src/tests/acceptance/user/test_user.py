import unittest
import openapi_client
from pprint import pprint
from src.tests.acceptance.helpers.client import client

class TestUser(unittest.TestCase):
    def test_create_get_user(self):
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
            id = api_response.result.id
            self.assertIsInstance(id, str)
            self.assertTrue(int(id) > 0)

            api_response = api_instance.user_service_get_user(id=id)
            print("The response of UsersApi->user_service_get_user:\n")
            pprint(api_response)
            self.assertIsNotNone(api_response)
            self.assertIsNotNone(api_response.result)
            self.assertIsNotNone(api_response.result.user)
            self.assertIsInstance(api_response.result.user.id, str)

            self.assertEqual(id, api_response.result.user.id)
            self.assertEqual(None, api_response.result.user.password)
            self.assertEqual("moto2", api_response.result.user.username)
            self.assertEqual("hello.moto@gmail.com", api_response.result.user.email)
            self.assertEqual("hello", api_response.result.user.first_name)
            self.assertEqual("moto", api_response.result.user.last_name)

if __name__ == '__main__':
    unittest.main()